import time

from rover import Rover
from servo import Servo
from cam import Camera
from dcmotors import Dcmotors
from reciever import Reciever
from buzzer import Buzzer

# Initialize the hardware components
motors: list[Dcmotors] = [
    Dcmotors(MOTOR_PIN1),
    Dcmotors(MOTOR_PIN2)
]
rf = Reciever(RECIEVER_PIN)
front_lidar = Lidar(TRIGGER_PIN, ECHO_PIN)
back_lidar = Lidar(TRIGGER_PIN, ECHO_PIN)
camera = Camera()
servos: list[Servo] = [
    Servo(PITCH, ROLL, SERVO_PIN1),
    Servo(PITCH, ROLL, SERVO_PIN2)
]
rover = Rover(front_lidar, back_lidar, camera, servos, motors, rf)

# Main loop
while True:

    cmds: list[str] = rover.process_rf_commands()

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
