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
        self.reciever: reciever = reciever

    def process_rf_commands(self) -> list[str]:
        return reciever.process_rf_message()

    def parse_commands(self):
        cmds = self.process_rf_commands()
        if cmds:
            for cmd in cmds:
                if cmd == "A1":
                    '''Turn Camera 60 degrees to the right'''
                    pass
                elif cmd == "B2":
                    '''Turn Camera 60 degrees to the left'''
                    pass
                elif cmd == "C3":
                    '''Take Picture'''
                    pass
                elif cmd == "D4":
                    '''Change camera mode from color to grayscale'''
                    pass
                elif cmd == "E5":
                    '''Change camera mode from grayscle to color'''
                    pass
                elif cmd == "F6":
                    '''Rotate image 180 degrees (flip upside down)'''
                    pass
                elif cmd == "G7":
                    '''Apply special effect filters'''
                    pass
                elif cmd == "H8":
                    '''Remove filters'''
                    pass
                else:
                    print('Command was not valid')
