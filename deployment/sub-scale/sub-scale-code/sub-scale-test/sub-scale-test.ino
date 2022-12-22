#include <Wire.h>
#include <MPU6050.h>
#include <Servo.h>

const uint8_t MPU_ADDRESS = 0x68;  // MPU6050 I2C address
const int SERVO_1_PIN = 9;
const int SERVO_2_PIN = 10;
const int MIN_ANGLE = 62;  // minimum allowed servo angle
const int MAX_ANGLE = 135;  // maximum allowed servo angle
const int motorPin1 = 5;
const int motorPin2 = 18;

MPU6050 accelgyro(MPU_ADDRESS);

Servo servo1;
Servo servo2;

void setup() {
  // Initialize I2C communication with the MPU6050
  // Wire.begin();

  accelgyro.initialize();

  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);

  servo1.attach(SERVO_1_PIN);
  servo2.attach(SERVO_2_PIN);

  Serial.begin(9600);

}

void loop() {

  // // Read accelerometer values
  int ax, ay, az;
  accelgyro.getAcceleration(&ax, &ay, &az);
 

    String command = "run";
    Serial.println(command);
    if (command == "run") {

      Serial.println("Running");

      digitalWrite(motorPin1, HIGH);  // turn on the motors
      digitalWrite(motorPin2, HIGH);

      delay(2000); // CORRE POR DOS SEGUNDOS

      digitalWrite(motorPin1, LOW);  // turn off the motors
      digitalWrite(motorPin2, LOW);

    } else if (command == "stop") {

      digitalWrite(motorPin1, LOW);  // turn off the motors
      digitalWrite(motorPin2, LOW);

    } else if (command == "stand"){

      float pitch = atan2(ay, az) * 180 / PI;
      float roll = atan2(-ax, az) * 180 / PI;

      // adjust the servo positions to level the platform
      servo1.write(90 + pitch);
      servo2.write(90 + roll);

    } else if (command == "rest") {

      servo1.write(90);  // reset the servo positions to the neutral position
      servo2.write(90);
    }
  
}

