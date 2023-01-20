import time
import math
import pwmio
import busio
import board
import adafruit_mpu6050
#from adafruit_motor import Servo

THRESHOLD = 15  # Threshold for detecting launch/landing
SERVO_1_PIN = 5  # Pin for first servo
SERVO_2_PIN = 6  # Pin for second servo

# Initialize I2C bus and MPU6050 sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mpu6050.MPU6050(i2c)

# Initialize the servo objects

#set_pinout(board.RASPBERRY_PI_4_GPIO_P1_PINOUT)
#servo1 = Servo(SERVO_1_PIN)
#servo2 = Servo(SERVO_2_PIN)

isLaunched = False  # Flag for launch/landing detection

while True:
    # Read accelerometer values
    ax = sensor.acceleration[0]
    ay = sensor.acceleration[1]
    az = sensor.acceleration[2]
    print(ax,ay,az)
    # Check if the rocket is launched/landed
    if not isLaunched and abs(az) > THRESHOLD:
        isLaunched = True
        # Code for launching goes here

    elif isLaunched and abs(az) <= THRESHOLD:
        isLaunched = False
        # Code for landing goes here

    # If the rocket is in flight, use the servo motors to self-level
    if isLaunched:
        # Calculate the angle of the rocket relative to the ground
        # using the accelerometer values
        roll = math.atan2(ay, az)
        pitch = math.atan2(-ax, az)

        # Use the servo motors to self-level the rocket
        #servo1.write(90 + roll * 180 / math.pi)
        #servo2.write(90 - roll * 180 / math.pi)

    time.sleep(1)