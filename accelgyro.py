from mpu6050 import mpu6050

sensor = mpu6050(0x68)

while True:

    accelerometer_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()
<<<<<<< HEAD
    print(accelerometer_data)
=======


>>>>>>> 3d2ab38533b9de69cbe7ed8dff115072d5e269e2
    ax = accelerometer_data.get('x')
    ay = accelerometer_data.get('y')
    az = accelerometer_data.get('z')

    gx = gyro_data.get('x')
    gy = gyro_data.get('y')
    gz = gyro_data.get('z')
