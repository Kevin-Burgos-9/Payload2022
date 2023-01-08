import time
import arducam

from rover import Rover
from lidar import Lidar
from servos import Servos

# Initialize the hardware components
front_lidar = Lidar(TRIGGER_PIN, ECHO_PIN)
back_lidar = Lidar(TRIGGER_PIN, ECHO_PIN)
camera = arducam.Camera()
servos = Servos(PITCH_SERVO_PIN, ROLL_SERVO_PIN)

# Create the rover object
rover = Rover(front_lidar, back_lidar, camera, servos)

# Main loop
while True:

     rover.process_rf_commands()
