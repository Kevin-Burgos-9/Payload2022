#include <Wire.h>
#include <MPU6050.h>
#include <Servo.h>

const int MPU_ADDRESS = 0x68;  // MPU6050 I2C address
const int X_AXIS = 0;  // X axis of the accelerometer
const int Y_AXIS = 1;  // Y axis of the accelerometer
const int Z_AXIS = 2;  // Z axis of the accelerometer
const int THRESHOLD = 15;  // Threshold for detecting launch/landing
const int SERVO_1_PIN = 5;  // Pin for first servo
const int SERVO_2_PIN = 6;  // Pin for second servo

MPU6050 accelgyro;
Servo servo1;
Servo servo2;

bool isLaunched = false;  // Flag for launch/landing detection

void setup() {
  // Initialize I2C communication with the MPU6050
  Wire.begin();
  accelgyro.initialize();

  // Initialize servo objects
  servo1.attach(SERVO_1_PIN);
  servo2.attach(SERVO_2_PIN);
}

void loop() {
  // Read accelerometer values
  int ax, ay, az;
  accelgyro.getAcceleration(&ax, &ay, &az);
  Serial.println("x: " + ax);
  Serial.print("printing");
  // Check if the rocket is launched/landed
  if (!isLaunched && abs(az) > THRESHOLD) {
    isLaunched = true;
    // Code for launching goes here
  } else if (isLaunched && abs(az) <= THRESHOLD) {
    isLaunched = false;
    // Code for landing goes here
  }

  // If the rocket is in flight, use the servo motors to self-level
  if (isLaunched) {
    // Calculate the angle of the rocket relative to the ground
    // using the accelerometer values
    float roll = atan2(ay, az);
    float pitch = atan2(-ax, az);

    // Use the servo motors to self-level the rocket
    servo1.write(90 + roll * 180 / PI);
    servo2.write(90 + pitch * 180 / PI);
  }
  delay(1000);
}
