#Raspberry Pi TB6612FNG Library
import pigpio

pi = pigpio.pi()

class Motor:
    in1 = ""
    in2 = ""
    pwm = ""
    standbyPin = ""

    #Defaults
    hertz = 1000
    reverse = False #Reverse flips the direction of the motor

    #Constructor
    def __init__(self, in1, in2, pwm, standbyPin, reverse):
        self.in1 = in1
        self.in2 = in2
        self.pwm = pwm
        self.standbyPin = standbyPin
        self.reverse = reverse

        pi.set_mode(in1, pigpio.OUTPUT)
        pi.set_mode(in2, pigpio.OUTPUT)
        pi.set_mode(pwm, pigpio.OUTPUT)
        pi.set_mode(standbyPin, pigpio.OUTPUT)
        pi.write(standbyPin, 1)

        self.p = pi.hardware_PWM(pwm, self.hertz, 0)

    #Speed from -100 to 100
    def drive(self, speed):
        #Negative speed for reverse, positive for forward
        #If necessary use reverse parameter in constructor
        dutyCycle = abs(speed) * 10000
        if self.reverse:
            dutyCycle = 1000000 - dutyCycle

        if speed > 0:
            pi.write(self.in1, 1)
            pi.write(self.in2, 0)
        else:
            pi.write(self.in1, 0)
            pi.write(self.in2, 1)

        self.p = pi.hardware_PWM(self.pwm, self.hertz, dutyCycle)

    def brake(self):
        self.p = pi.hardware_PWM(self.pwm, self.hertz, 0)
        pi.write(self.in1, 1)
        pi.write(self.in2, 1)

    def standby(self, value):
        self.p = pi.hardware_PWM(self.pwm, self.hertz, 0)
        pi.write(self.standbyPin, value)

    def __del__(self):
        pi.stop()
