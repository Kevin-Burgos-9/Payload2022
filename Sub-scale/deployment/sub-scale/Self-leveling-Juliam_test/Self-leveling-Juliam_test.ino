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

int minTresh1 = 65;
int maxTresh1 = 135;
int minTresh2 = 65;
int maxTresh2 = 135;
bool initial = true;
bool balanced = false;

void setup() {
    // Initialize I2C communication with the MPU6050
  Wire.begin();

  accelgyro.initialize();

  // pinMode(motorPin1, OUTPUT);
  // pinMode(motorPin2, OUTPUT);

  servo1.attach(SERVO_1_PIN);
  servo2.attach(SERVO_2_PIN);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    int ax, ay, az;
    accelgyro.getAcceleration(&ax, &ay, &az);

    float pitch = atan2(ay, az) * 180 / PI; // pitch will be in the range of -3.00 and 3.00, -1.5 and 1.5 are vertical positions

    if (initial == true){
      servo1.write(minTresh1);
      servo2.write(minTresh2);
      initial = false;
    }

    if (pitch == 1.50){balanced = true;}

    if (pitch != 1.50 && balanced == false){

        if(pitch > 1.50){
          minTresh1++;
          servo1.write(minTresh1);
        }
        if(pitch < 1.50){
          minTresh2++;
          servo2.write(minTresh2);
        }
    }














}
