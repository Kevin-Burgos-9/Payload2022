import time
import pigpio

# Initialize pigpio
pi = pigpio.pi()

# Choose GPIO pin for the buzzer
GPIO = 4

# Set the frequency of the buzzer
frequency = 500

# Set the duty cycle to 50%
duty_cycle = 128


def buzzer_on():
    pi.set_PWM_dutycycle(GPIO, duty_cycle)
    pi.set_PWM_frequency(GPIO, frequency)
    time.sleep(0.5)

    # Turn off the buzzer
    pi.set_PWM_dutycycle(GPIO, 0)
    time.sleep(10)
