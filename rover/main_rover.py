import time

from rover import Rover
# from servo import Servo
# from cam import Camera
# from dcmotors import Dcmotors
# from reciever import Reciever
# from buzzer import Buzzer
#
# # Initialize the hardware components
# motors: list[Dcmotors] = [
#     Dcmotors(MOTOR_PIN1),
#     Dcmotors(MOTOR_PIN2)
# ]
# rf = Reciever(RECIEVER_PIN)
# front_lidar = Lidar(TRIGGER_PIN, ECHO_PIN)
# back_lidar = Lidar(TRIGGER_PIN, ECHO_PIN)
# camera = Camera()
# servos: list[Servo] = [
#     Servo(PITCH, ROLL, SERVO_PIN1),
#     Servo(PITCH, ROLL, SERVO_PIN2)
# ]
# rover = Rover(front_lidar, back_lidar, camera, servos, motors, rf)

# Main loop
while True:

    # Buzzer beeping un separate thread every 1 second <- AlWAYS beeping

    # accelerometer is detecting launch and landing
    # When acc changes, launch = True
    # Acc is constant for 3 seconds, landing = True
        # Orientation awareness begin
        # Wi-Fi connected to retention sends the deployment signal
        # Released signal received, motors move one direction until out of retention
            # Use LiDAR to identify that it is outside
        # Motors switch rotation depending on orientation
        # Gyro finds a leveled surface
            # Self-leveling starts
            # Self-leveled = True
                # Listen for RF signals
                # Execute commands


