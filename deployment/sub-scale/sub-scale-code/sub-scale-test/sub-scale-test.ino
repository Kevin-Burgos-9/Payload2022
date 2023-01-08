#include <Wire.h>
#include <MPU6050.h>
#include <Servo.h>

const uint8_t MPU_ADDRESS = 0x68; // MPU6050 I2C address
const int SERVO_1_PIN = 9;
const int SERVO_2_PIN = 10;
const int MIN_ANGLE = 62;  // minimum allowed servo angle
const int MAX_ANGLE = 135; // maximum allowed servo angle
const int motorPin1 = 5;
const int motorPin2 = 18;

float AccX, AccY, AccZ;

MPU6050 accelgyro(MPU_ADDRESS);

Servo servo1;
Servo servo2;

void setup()
{
  Serial.begin(115200);
  Wire.begin();                        // Initialize comunication
  Wire.beginTransmission(MPU_ADDRESS); // Start communication with MPU6050 // MPU=0x68
  Wire.write(0x6B);                    // Talk to the register 6B
  Wire.write(0x00);                    // Make reset - place a 0 into the 6B register
  Wire.endTransmission(true);

  servo1.attach(SERVO_1_PIN);
  servo2.attach(SERVO_2_PIN);
}

void loop()
{
  Wire.beginTransmission(MPU_ADDRESS);
  Wire.write(0x3B); // Start with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_ADDRESS, 6, true); // Read 6 registers total, each axis value is stored in 2 registers
  // For a range of +-2g, we need to divide the raw values by 16384, according to the datasheet
  Serial.println(AccX);

  AccX = (Wire.read() << 8 | Wire.read()) / 16384.0; // X-axis value
  AccY = (Wire.read() << 8 | Wire.read()) / 16384.0; // Y-axis value
  AccZ = (Wire.read() << 8 | Wire.read()) / 16384.0; // Z-axis value

  float pitch = atan2(AccY, AccZ) * 180 / PI;
  float roll = atan2(-AccX, AccZ) * 180 / PI;

  servo1.write(90 + pitch);
  servo2.write(90 - pitch);

  //  servo1.write(130);

  //  Serial.println(AccX);
}
