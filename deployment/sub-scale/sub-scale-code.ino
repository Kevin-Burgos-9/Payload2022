#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
Adafruit_MPU6050 mpu;
void setup(void) {
  Serial.begin(115200);
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens
  Serial.println("Adafruit MPU6050 test!");
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");
  //setupt motion detection
  mpu.setHighPassFilter(MPU6050_HIGHPASS_0_63_HZ);
  mpu.setMotionDetectionThreshold(1);
  mpu.setMotionDetectionDuration(20);
  mpu.setInterruptPinLatch(true);	// Keep it latched.  Will turn off when reinitialized.
  mpu.setInterruptPinPolarity(true);
  mpu.setMotionInterrupt(true);
  Serial.println("");
  delay(100);
}

uint8_t motor_pin = 3;
bool is_launched = false;

void launched(uint8_t acc){
  if(acc >= 13){
    is_launched = true;
  }
}

void loop() {

  uint8_t total_accel = a.acceleration.x + a.acceleration.y + a.acceleration.z;
  launched(total_accel);

  if(is_launched){
  
    if(!mpu.getMotionInterruptStatus()) { //No motion detected and the payload has arrived.

      //Activate motor for 5 seconds
      Serial.println("ARRIVED");
    }
  }

  if(mpu.getMotionInterruptStatus()) {
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);
    Serial.println(a.acceleration.x + a.acceleration.y + a.acceleration.z);
  }
  else{
    Serial.println("NO MOTION DETECTED");
    delay(1000);
  }
  delay(10);
}
