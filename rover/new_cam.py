import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Reset the ESP32
ser.write(b'\x3F\x3F\x3F')
time.sleep(1)

# Start the camera
ser.write(b'X')

# Wait for the camera to initialize
time.sleep(1)

# Take a picture
ser.write(b'Y')
time.sleep(1)

# Read the picture data
data = b''
while True:
    b = ser.read()
    if b == b'\xFF':
        data += b
        break
    data += b

# Save the picture to a file
with open('picture.jpg', 'wb') as f:
    f.write(data)

# Stop the camera
ser.write(b'Z')
ser.close()
