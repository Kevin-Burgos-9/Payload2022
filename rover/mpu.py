from mpu6050 import mpu6050
import math

mpu = mpu6050(0x68)

def checkTilt(aX, aY, aZ):

    pitch = math.atan2(-1 * aX, aZ) * 180 / math.pi # rotation on Y axis
    roll = math.atan2(-1 * (aY), aZ) * 180 / math.pi # rotation on X axis   

    return (pitch, roll)



while True:

    accelerometer_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()

    ax = accelerometer_data.get('x')
    ay = accelerometer_data.get('y')
    az = accelerometer_data.get('z')

    print(checkTilt(ax, ay, az))