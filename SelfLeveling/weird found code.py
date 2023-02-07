#Include the library files
import RPi.GPIO as GPIO
import smbus 
from time import sleep

# Setup GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# Set the servo motor pin as output pin
GPIO.setup(32,GPIO.OUT)

pwm = GPIO.PWM(32,50)
pwm.start(0)

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT = 0x3B
ACCEL_YOUT = 0x3D
ACCEL_ZOUT = 0x3F
GYRO_XOUT  = 0x43
GYRO_YOUT  = 0x45
GYRO_ZOUT  = 0x47


bus = smbus.SMBus(1) # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68 # MPU6050 device address

def angle(Angle):
    duty = Angle / 18 + 2
    GPIO.output(32,True)
    pwm.ChangeDutyCycle(10)
    sleep(1)
    GPIO.output(32,False)
    pwm.ChangeDutyCycle(0)
    
def setAngle():
    angle(90)

angle(300)
    

