from mpu6050 import mpu6050
from gpiozero import Buzzer
import math
import time
import record
from datetime import datetime


mpu = mpu6050(0x68)
buzzer = Buzzer(4)  # enter GPIO pin


def checkTilt(aX, aY, aZ):

    pitch = math.atan2(-1 * aX, aZ) * 180 / math.pi  # rotation on Y axis
    roll = math.atan2(-1 * (aY), aZ) * 180 / math.pi  # rotation on X axis

    if abs(roll) > 90 or abs(pitch) > 90:
        return "Rover is upside down"
    elif (roll > 0 and pitch < 0) or (roll < 0 and pitch > 0):
        return "Rover is upside down"
    else:
        return "Rover is not upside down"


mpu.set_accel_range(mpu.ACCEL_RANGE_16G)

landCheck = False

landCount = 0

while True:

    LANDED = False
    temperature = 0

    accelerometer_data = mpu.get_accel_data(g=True)
    gyro_data = mpu.get_gyro_data()

    if round(accelerometer_data.get('x'), 1) > 4 or round(accelerometer_data.get('x'), 1) < -4:
        landCheck= True
        print("Launched")

    prevX = round(accelerometer_data.get('x'), 1)
    prevY = round(accelerometer_data.get('y'), 1)
    prevZ = round(accelerometer_data.get('z'), 1)

    time.sleep(0.05)

    accelerometer_data = mpu.get_accel_data(g=True)
    ax = round(accelerometer_data.get('x'), 1)
    ay = round(accelerometer_data.get('y'), 1)
    az = round(accelerometer_data.get('z'), 1)

    print('X: ' + str(prevX) + ' Y: ' + str(prevY) + ' Z: ' + str(prevZ))
    print('X: ' + str(ax) + ' Y: ' + str(ay) + ' Z: ' + str(az))

    if landCheck:
        # LANDED CODE
        if (ax == prevX) and (ay == prevY) and (az == prevZ):
            print('Landed!!!')
            landCount += 1
            if landCount >= 15:
                LANDED = True
            print(checkTilt(ax, ay, az))

        # NOT LANDED, STILL MOVING
        else:
            print('Schmooving!')
            LANDED = False

    temp = []
    date_str = str(datetime.now())

    current_time = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    t = time.localtime()
    # current_time = time.strftime("%M:%S", t)

    temperature = mpu.get_temp()

    temp.append(current_time)
    temp.append(ax)
    temp.append(ay)
    temp.append(az)
    temp.append(LANDED)
    temp.append(temperature)

    pitch = math.atan2(-1 * ax, az) * 180 / math.pi  # rotation on Y axis
    temp.append(pitch)
    roll = math.atan2(-1 * (ay), az) * 180 / math.pi  # rotation on X axis
    temp.append(roll)

    print(checkTilt(ax, ay, az))

    if LANDED:

        print("Landed")

        # Record one more time for statistics
        record.record(temp)

       while True:
            buzzer.on()

        exit()
    else:
        record.record(temp)

    buzzer.on()
    time.sleep(0.5)
    buzzer.off()
