import TB6612FNG
import adafruit_mpu6050
import RadioHead
from reciever import reciever

class Rover:
    def __init__(self, front_lidar, back_lidar, camera, servos, reciever):
        self.driver = TB6612FNG.Driver()
        self.front_lidar = front_lidar
        self.back_lidar = back_lidar
        self.mpu = adafruit_mpu6050.MPU6050()
        self.camera = camera
        self.servos = servos
        self.arms_deployed = False
        self.leveled = False
        self.reciever : reciever = reciever

    def process_rf_commands() -> list[str]:
        return reciever.process_rf_message()


