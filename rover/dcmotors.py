import pigpio


class Motor:
    def __init__(self, pwm_pin, stby_pin, in1_pin, in2_pin):
        self.pwmA = pwm_pin
        self.stby = stby_pin
        self.aIn1 = in1_pin
        self.aIn2 = in2_pin

        self.pi = pigpio.pi()

        # Setting pins to output
        self.pi.set_mode(self.pwmA, pigpio.OUTPUT)
        self.pi.set_mode(self.stby, pigpio.OUTPUT)
        self.pi.set_mode(self.aIn1, pigpio.OUTPUT)
        self.pi.set_mode(self.aIn2, pigpio.OUTPUT)

        # 1 -> High, this enables the driver
        self.pi.write(stby_pin, 1)

    def motorBackward(self):
        self.pi.write(self.aIn, 0)
        self.pi.wite(self.aIn2, 1)

    def motorForward(self):
        # in1 and in2 control the polarity
        self.pi.write(self.aIn1, 1)
        self.pi.write(self.aIn2, 0)
        self.pi.set_PWM_dutycycle(self.pwmA, 256)  # set motor speed to 100%

    def avoid(self):
        pass

    def motorStop(self):
        self.pi.write(self.aIn1, 0)
        self.pi.write(self.aIn2, 0)
        self.pi.set_PWM_dutycycle(self.pwmA, 0)  # set motor speed to 0

    