from mpu6050 import mpu6050
import math
import time
import record.py


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

    prevX = round(accelerometer_data.get('x'),0)
    prevY = round(accelerometer_data.get('y'),0)
    prevZ = round(accelerometer_data.get('z'),0)

    time.sleep(0.5)

    accelerometer_data = mpu.get_accel_data()
    ax = round(accelerometer_data.get('x'),0)
    ay = round(accelerometer_data.get('y'),0)
    az = round(accelerometer_data.get('z'),0)

    print('X: ' + str(prevX) + ' Y: ' + str(prevY) + ' Z: '+ str(prevZ))
    print('X: ' + str(ax) + ' Y: ' + str(ay) + ' Z: '+ str(az))


    #LANDED CODE
    if (ax == prevX) and (ay == prevY) and (az == prevZ):
        print('Landed!!!')
        print(checkTilt(ax, ay, az))
    
    #NOT LANDED, STILL MOVING
    else:
        print('Schmooving!')

    temp = []
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    temp.append(current_time)
    temp.append(ax)
    temp.append(ay)
    temp.append(az)

    print(checkTilt(ax, ay, az))

    record(temp)

    time.sleep(0.5)
