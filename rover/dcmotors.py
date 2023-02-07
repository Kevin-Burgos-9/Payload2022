from gpiozero import Motor
from mpu6050 import mpu6050

mpu = mpu6050(0x68)

accelerometer_data = sensor.get_accel_data()

class Dcmotors:
    def __init__(self, motor_pin: int):
        self.motor_pin = motor_pin
        self.motor = Motor(motor_pin)

    def isOn(self) -> bool:
        """ Detects if the motor is turned on """

        return self.motor.is_active

    def getPin(self) -> int:

        return self.motor_pin

    def isStuck(self) -> bool:





        



    def move_rover(self, backwards: bool) -> None:



        """Function to move rover forward,
        unless the backwards boolean is true, then move backwards"""
        pass

    def rotate_rover(self, left: bool) -> None:
        """Function to move rover to the right,
        unlessthe left boolean is true, then rotate left"""
        pass
