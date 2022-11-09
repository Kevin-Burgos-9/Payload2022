import time

import RPi.GPIO as GPIO

OUT_PIN = 11
PULSE_FREQ = 50

GPIO.setmode(GPIO.BOARD)
GPIO.setup(OUT_PIN, GPIO.OUT)


def main():
    print("Starting")
    servo1 = GPIO.PWM(OUT_PIN, PULSE_FREQ)

    servo1.start(0)

    print("Spinning")

    # Test the full range of movement. Note only integers are allowed.
    for x in range(2, 12):
        servo1.ChangeDutyCycle(x)
        time.sleep(0.5)

    # Start over and move in bigger, slower movements.
    servo1.ChangeDutyCycle(2)
    time.sleep(1)
    servo1.ChangeDutyCycle(7)
    time.sleep(1)
    servo1.ChangeDutyCycle(12)
    time.sleep(4)

    # Jump between the opposite positions.
    servo1.ChangeDutyCycle(2)
    time.sleep(1)
    servo1.ChangeDutyCycle(12)
    time.sleep(1)
    servo1.ChangeDutyCycle(2)
    time.sleep(1)
    servo1.ChangeDutyCycle(12)
    time.sleep(4)

    # Test the fastest movement possible - no sleeping.
    servo1.ChangeDutyCycle(2)
    servo1.ChangeDutyCycle(12)
    servo1.ChangeDutyCycle(2)
    servo1.ChangeDutyCycle(12)
    servo1.ChangeDutyCycle(2)
    servo1.ChangeDutyCycle(12)
    servo1.ChangeDutyCycle(2)
    servo1.ChangeDutyCycle(12)

    servo1.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    main()