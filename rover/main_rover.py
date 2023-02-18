import time
import buzzer
import keyboard
import dcmotors as motor

motor1 = motor.Motor(pwm_pin=6, stby_pin=25, in1_pin=24, in2_pin=23)
motor2 = motor.Motor(pwm_pin=17, stby_pin=25, in1_pin=22, in2_pin=16)

while True:
    user_input = input("Please enter a command: ")

    while not keyboard.is_pressed('space'):

        if user_input == "1":

            buzzer.buzzer_on()

        elif user_input == "2":

            motor1.motor_forward()
            motor2.motor_forward()

            time.sleep(3)

            motor1.motor_stop()
            motor2.motor_stop()

        else:
            print("Invalid command. Please try again.")
        keyboard.wait()

    break
