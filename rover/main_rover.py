import buzzer

while True:

    selection = input("Option: ")
    if selection == '1':
        buzzer.buzzer_on()