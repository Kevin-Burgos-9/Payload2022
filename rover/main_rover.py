import buzzer
import keyboard

while True:
    user_input = input("Please enter a command: ")

    while not keyboard.is_pressed():
        if user_input == "1":
            buzzer.buzzer_on()
        elif user_input == "2":
            print("Command 2 executed!")
        else:
            print("Invalid command. Please try again.")
        keyboard.wait()

    break
