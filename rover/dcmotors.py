from gpiozero import Motor
from mpu6050 import mpu6050
from RpiMotorLib import rpi_dc_lib


mpu = mpu6050(0x68)
gyro_data = sensor.get_accel_data()

//PINS FOR DRIVER
PWA = 17
AI1 = 22
AI2 = 27
PWB = 18
BI1 = 23
BI2 = 24
Standby = 25
Freq = 50

//MOTOR OBJECTS USING DRIVER
motor_one = rpi_dc_lib.TB6612FNGDc(AI1 ,AI2 ,PWA ,Freq,True, "motor_one")
motor_two = rpi_dc_lib.TB6612FNGDc(BI1 ,BI2 ,PWB ,Freq ,True, "motor_two")

class Dcmotors:
    def __init__(self, motor_pin: int):
        self.motor_pin = motor_pin
        self.motor = Motor(motor_pin)
        self.side = side
        
    def isOn(self) -> bool:
        """ Detects if the motor is turned on """

        return self.motor.is_active

    def getPin(self) -> int:

        return self.motor_pin

    def isStuck(self) -> bool:
        
        //check if motors are turned on

        if isOn:
            
            //Check if the gyroscope data is constant

                //Check if the accelerometer doesnt pass threshold



    def move_rover(self, backwards: bool) -> None:

        if backwards:

            motor_one.backward(25)
            motor_two.backward(25)

        else:

            motor_one.forward(25)
            motor_one.forward(25)

    def rotate_rover(self, left: bool) -> None:
        """Function to move rover to the right,
        unlessthe left boolean is true, then rotate left"""
        pass
