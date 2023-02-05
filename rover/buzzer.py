import RPi.GPIO as GPIO
import time


class Buzzer:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)
        self.buzzer_pin = pin
        GPIO.setup(self.buzzer_pin, GPIO.OUT)

    def buzzer_on(self):
        GPIO.output(self.buzzer_pin, GPIO.HIGH)

    def buzzer_off(self):
        GPIO.output(self.buzzer_pin, GPIO.LOW)

    def different_tones_example(self):
        p = GPIO.PWM(self.buzzer_pin, 50)
        while True:
            for f in np.linspace(200, 2000, num=50): # Numpy needed
                p.ChangeFrequency(f)
                time.sleep(0.01)
