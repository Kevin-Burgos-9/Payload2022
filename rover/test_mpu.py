from mpu6050 import mpu6050

mpu6050_sensor = mpu6050(0x68)  # MPU6050 device address

while True:
    # Read accelerometer data
    accel_data = mpu6050_sensor.get_accel_data()

    # Print acceleration data
    print("Acceleration in X-Axis : %f g" % accel_data['x'])
    print("Acceleration in Y-Axis : %f g" % accel_data['y'])
    print("Acceleration in Z-Axis : %f g" % accel_data['z'])
