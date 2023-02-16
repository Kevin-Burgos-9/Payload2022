from motor import *
from time import sleep #Only used for example
import pigpio

pi = pigpio.pi()

#Motor(IN1,IN2,PWM,STANDBY,(Reverse polarity?))
test = Motor(16,18,31,6,False)

test.drive(100) #Forward 100% dutycycle
sleep(1)
test.drive(-100) #Backwards 100% dutycycle
sleep(1)
test.brake() #Short brake
sleep(0.1)

test.standby(True) #Enable standby
test.standby(False) #Disable standby