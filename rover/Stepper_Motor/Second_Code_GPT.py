import RPi.GPIO as GPIO
import time

# Define stepper motor pins
step_pin = 18
dir_pin = 23

# Set GPIO mode and pins as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)

# Set initial motor direction
GPIO.output(dir_pin, GPIO.HIGH)

# Define motor speed and steps per revolution
motor_speed = 10 # in revolutions per minute
steps_per_rev = 512

# Calculate delay time based on motor speed
delay_time = 60.0 / (steps_per_rev * motor_speed)

# Step motor forward for 1 revolution
for i in range(steps_per_rev):
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(delay_time/2)
    GPIO.output(step_pin, GPIO.LOW)
    time.sleep(delay_time/2)

# Set motor direction
GPIO.output(dir_pin, GPIO.LOW)

# Step motor backward for 1 revolution
for i in range(steps_per_rev):
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(delay_time/2)
    GPIO.output(step_pin, GPIO.LOW)
    time.sleep(delay_time/2)

# Cleanup GPIO pins
GPIO.cleanup()
