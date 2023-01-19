import time

from rover import Rover

from servo import servo
from cam import camera
from dcmotors import dcmotors
from reciever import reciever
from buzzer import buzzer

# Initialize the hardware components
front_lidar = Lidar(TRIGGER_PIN, ECHO_PIN)
back_lidar = Lidar(TRIGGER_PIN, ECHO_PIN)
camera = arducam.Camera()
servos = Servos(PITCH_SERVO_PIN, ROLL_SERVO_PIN)

# Create the rover object
rover = Rover(front_lidar, back_lidar, camera, servos)

# Main loop
while True:

     cmds : list[str] = rover.process_rf_commands()
     
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