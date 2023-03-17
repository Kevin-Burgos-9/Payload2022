#include <Wire.h>
#include <MPU6050.h>

MPU6050 imu;
int16_t ax, ay, az;

const float GRAVITY = 9.81; // m/s^2
const float MAX_SPEED = 152.4; // m/s = 500 ft/s

bool launched = false;
bool landed = false;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  imu.initialize();
}

void loop() {
  imu.getAcceleration(&ax, &ay, &az);
  float acc = sqrt(pow(ax, 2) + pow(ay, 2) + pow(az, 2)) / 16384.0; // convert to m/s^2
  float altitude = (acc - GRAVITY) * pow(micros() / 1000000.0, 2) / 2.0; // calculate altitude based on acceleration
  Serial.print("Acceleration: ");
  Serial.print(acc);
  Serial.print(" m/s^2, Altitude: ");
  Serial.print(altitude);
  Serial.println(" m");

  if (acc > GRAVITY + 5.0 && !launched) { // detect launch
    Serial.println("Rocket launched!");
    launched = true;
  }

  if (altitude < 0.0 && !landed && launched) { // detect landing
    Serial.println("Rocket landed!");
    landed = true;
  }

  if (acc > MAX_SPEED && !landed && launched) { // detect max speed
    Serial.println("Maximum speed exceeded!");
  }

  delay(10); // wait 10ms before next reading
}
