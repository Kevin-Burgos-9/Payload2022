from mpu6050 import mpu6050
import math
import time
from csv import writer

mpu = mpu6050(0x68)

def checkTilt(aX, aY, aZ):

    pitch = math.atan2(-1 * aX, aZ) * 180 / math.pi # rotation on Y axis
    roll = math.atan2(-1 * (aY), aZ) * 180 / math.pi # rotation on X axis   

    if abs(roll) > 90 or abs(pitch) > 90:
        return "Robot is upside down"
    elif (roll > 0 and pitch < 0) or (roll < 0 and pitch > 0):
       return "Robot is upside down"
    else:
        return "Robot is not upside down"


while True:

    accelerometer_data = mpu.get_accel_data()
    gyro_data = mpu.get_gyro_data()

    ax = accelerometer_data.get('x')
    ay = accelerometer_data.get('y')
    az = accelerometer_data.get('z')

    temp = []
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    temp.append(current_time)
    temp.append(ax)
    temp.append(ay)
    temp.append(az)

    print(checkTilt(ax, ay, az))

    with open('data.csv', 'a') as dataFile:
        fileObject = writer(dataFile)
        fileObject.writerow(temp)
        fileObject.close()

    time.sleep(0.5)
