from mpu6050 import mpu6050
import math
import time
import record


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

mpu.set_accel_range(mpu6050_sensor.ACCEL_RANGE_16G)

okidokiToRecordy = False    

while True:

    LANDED = False
    temperature = 0

    accelerometer_data = mpu.get_accel_data(g=True)
    gyro_data = mpu.get_gyro_data()

    if accelerometer_data.get('x') > 3.0:
        okidokiToRecordy = True

    if okidokiToRecordy:
        prevX = round(accelerometer_data.get('x'),0)
        prevY = round(accelerometer_data.get('y'),0)
        prevZ = round(accelerometer_data.get('z'),0)

        time.sleep(0.15)

        accelerometer_data = mpu.get_accel_data()
        ax = round(accelerometer_data.get('x'),0)
        ay = round(accelerometer_data.get('y'),0)
        az = round(accelerometer_data.get('z'),0)

        print('X: ' + str(prevX) + ' Y: ' + str(prevY) + ' Z: '+ str(prevZ))
        print('X: ' + str(ax) + ' Y: ' + str(ay) + ' Z: '+ str(az))


        #LANDED CODE
        if (ax == prevX) and (ay == prevY) and (az == prevZ):
            print('Landed!!!')
            LANDED = True
            print(checkTilt(ax, ay, az))
        
        #NOT LANDED, STILL MOVING
        else:
            print('Schmooving!')
            LANDED = False

        temp = []
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        
        temperature = mpu.get_temp()

        temp.append(current_time)
        temp.append(ax)
        temp.append(ay)
        temp.append(az)
        temp.append(LANDED)
        temp.append(temperature)

        print(checkTilt(ax, ay, az))

        record.record(temp)

        time.sleep(0.5)
