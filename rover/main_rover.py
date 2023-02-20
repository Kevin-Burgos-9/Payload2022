import time
import buzzer
import keyboard
import dcmotors as motor

motor1 = motor.Motor(pwm_pin=6, stby_pin=25, in1_pin=24, in2_pin=23)
motor2 = motor.Motor(pwm_pin=17, stby_pin=25, in1_pin=22, in2_pin=16)

while True:
    userInput = input("Please enter a command: ")

    while not keyboard.is_pressed('space'):

        if userInput == "1":

            buzzer.buzzer_on()

        elif userInput == "2":

            motor1.motorForward()
            motor2.motorForward()

            time.sleep(3)

            motor1.motorStop()
            motor2.motorStop()

        else:
            print("Invalid command. Please try again.")
        keyboard.wait()

    break
