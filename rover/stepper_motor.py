import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
DIR = 27
STEP = 22
CW = 1
CCW = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# Set the direction

def step_motor(direction, angle, delay):
    # Convert angle to number of steps
    STEPS_PER_REV = 2048
    steps = int(angle / 360 * STEPS_PER_REV)

    # Set the direction of rotation
    if direction == 1:
        GPIO.output(DIR, CW)
    else:
        GPIO.output(DIR, CCW)

    # Step the motor
    for i in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(delay)

# Example usage
step_motor(1, 60, 0.001)
time.sleep(3)
step_motor(0,60, 0.001)
time.sleep(1)
step_motor(1,360,0.001)
# Clean up the GPIO pins
GPIO.cleanup()
