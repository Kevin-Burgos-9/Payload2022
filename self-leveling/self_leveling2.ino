/*
 * Accelerator demo
 * 
 */
#include <Servo.h>
#include <Adafruit_ADXL345_U.h>

// Create servo objects for x and y servos
Servo xServo;
Servo yServo;

// Used to level the platform, if needed
int xOffset = -7;
int yOffset = -1;

// Used to decrease sensitivity
int sensitivity = 50;

// Assign a unique ID to this sensor at the same time
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);


void setup() {
      Serial.begin(9600);
  
// Initialize sensor
      if(!accel.begin())
      {
// Sensor not detected
            Serial.println("No Sensor detected");
      while(1);

      }

// Connect servos to pins
      xServo.attach(9);
      yServo.attach(10);

// Setup sensor Range and datarate
      accel.setRange(ADXL345_RANGE_16_G);
      accel.setDataRate(ADXL345_DATARATE_25_HZ);

}

void loop() {
 
      sensors_event_t event; 
      accel.getEvent(&event);

// Get x and y values from sensor
      int x = event.acceleration.x;
      int y = event.acceleration.y;

// map sensor value (-10 - 10) to servo position value (30 - 150)
      int x1 = map(x, -10, 10, 130, 50);
      int y1 = map(y, -10, 10, 50, 130);

// Troubleshoot info - show sensor reading and mapping
      Serial.print("X: "); Serial.print(x);
      Serial.print("\tY: "); Serial.print(y);
      Serial.print("\tX1: "); Serial.print(x1);
      Serial.print("\tY1: "); Serial.println(y1);

// move servos based on sensor mapping
      xServo.write(x1 + xOffset);
      yServo.write(y1 + yOffset);
      delay(sensitivity);         //delay to decrease sensitivity
}
