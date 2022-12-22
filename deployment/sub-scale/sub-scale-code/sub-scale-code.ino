#include <Wire.h>
#include <MPU6050.h>
#include <Servo.h>

const uint8_t MPU_ADDRESS = 0x68;  // MPU6050 I2C address
const int X_AXIS = 0;  // X axis of the accelerometer
const int Y_AXIS = 1;  // Y axis of the accelerometer
const int Z_AXIS = 2;  // Z axis of the accelerometer
const int LAUNCHED_THRESHOLD = 25000;  // Threshold for detecting launch/landing
const int LANDED_THRESHOLD_MIN = 12500;
const int LANDED_THRESHOLD_MAX  = 15500;
const int SERVO_1_PIN = 9;  // Pin for first servo
const int SERVO_2_PIN = 6;  // Pin for second servo


const int MIN_ANGLE = 62;  // minimum allowed servo angle
const int MAX_ANGLE = 135;  // maximum allowed servo angle


MPU6050 accelgyro(MPU_ADDRESS);
Servo servo1;
//Servo servo2;

bool isLaunched = true;  // Flag for launch/landing detection
bool isLanded = false;
void setup() {
  // Initialize I2C communication with the MPU6050
  Wire.begin();
  accelgyro.initialize();
  Serial.println(accelgyro.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");
  // servo1.write(20);

  // Initialize servo objects
  if(isLanded){
  servo1.attach(SERVO_1_PIN);
  servo1.write(MIN_ANGLE);
  }
  

  //servo2.attach(SERVO_2_PIN);
}


void loop() {

  // Read accelerometer values
  int ax, ay, az;
  accelgyro.getAcceleration(&ax, &ay, &az);
  Serial.print("accel values:\n");
  Serial.print(ax); Serial.print("\t");
  Serial.print(ay); Serial.print("\t");
  Serial.print(az); Serial.print("\t");
  Serial.print("\n");
  // Check if the rocket is launched
  if(!isLaunched){
    Serial.println("The rocket has not launched yet.");
  }

  if (!isLaunched && abs(ay) > LAUNCHED_THRESHOLD) {
    isLaunched = true;

    // Code for launching goes here

  } else if (isLaunched && abs(ay) <= LAUNCHED_THRESHOLD) {
    isLaunched = false;

  }

  if(isLaunched && abs(az) >= LANDED_THRESHOLD_MIN && abs(az) <= LANDED_THRESHOLD_MAX){

    // CODE WHEN ROCKET HAS LANDED.
    isLanded = true;
  }


  // If the rocket is in flight, use the servo motors to self-level
  if (isLaunched) {
    // Calculate the angle of the rocket relative to the ground
    // using the accelerometer values
    float roll = atan2(ay, az);
    float pitch = atan2(-ax, az);

    // Use the servo motors to self-level the rocket
    // servo1.write(90 - pitch * 180 / PI);
    //servo2.write(90 + pitch * 180 / PI);
  }

  delay(1000);
}

