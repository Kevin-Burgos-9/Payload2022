from mpu6050 import mpu6050
import RPi.GPIO as GPIO
import time
import math

class SelfLeveling():
    def __init__(self):
        self.rightLegAngle = 90
        self.leftLegAngle = 90
        self.leveled = False
        self.p1 = GPIO.PWM(12, 50)
        self.p2 = GPIO.PWM(13, 50)
        self.p1.start(0)
        self.p2.start(0)


    def get_pwm(self, angle):
        return (angle/18.0) + 2.5
    
    def set_straight(self):
        self.p1.ChangeDutyCycle(self.get_pwm(90))
        self.p2.ChangeDutyCycle(self.get_pwm(90))
        time.sleep(1)
        self.p1.start(0) # Reduces jitter, must have a time.sleep 
        self.p2.start(0)
        
    
    def level(self,pitch):
        if pitch <= -2 and pitch >= -3:
            self.p1.start(0) # Reduces jitter, must have a time.sleep 
            self.p2.start(0)
            self.leveled = True
        
        elif pitch > -2:
            self.rightLegAngle += 1
            self.p1.ChangeDutyCycle(self.get_pwm(self.rightLegAngle))
       
        elif pitch < -3:
            self.leftLegAngle += 1
            self.p2.ChangeDutyCycle(self.get_pwm(self.leftLegAngle))

mpu = mpu6050(0x68)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

#in main loop, if mpu data is too far from ideal, then restart the process
l = SelfLeveling()
l.set_straight()
while True:
    ax = mpu.get_accel_data().get("x")
    ay = mpu.get_accel_data().get("y")
    az = mpu.get_accel_data().get("z")
    print(ax,ay,az)
    #pitch = math.atan2(-ax, az) ignore for now, working with az
    #print(pitch)
    
    if l.leveled == False:
        l.level(az)
        
    if az > -2 or az < -3:
        l.leveled = False
    



   

    
GPIO.cleanup()
