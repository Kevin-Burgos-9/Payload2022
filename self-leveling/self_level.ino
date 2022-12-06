// Video -> https://www.youtube.com/watch?v=XJlWqhm8Jw8

#include <Servo.h>

Servo myservo1, myservo2, myservo3, myservo4;  // create servo object to control a servo

int potpin = 0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin
int gyroPin = 3; //tiltmeter VTI SCA610 inclinometer chip (accelerometer)
int gyroPin2 = 5; //tiltmeter VTI SCA610 inclinometer chip (accelerometer)
int fRServo,fLServo,rRServo,rLServo;
int frontTilt;
int sideTilt;
int lowBoy = 1;
///////////////////////////////////////////////////
// this routine controls the speed of the servo 
/////////////////////////////////////////////////
void myServo(int newAngle,int angleInc,int incDelay,int servoNum) {
  int curAngle;
  if (servoNum== 1) {  curAngle = myservo1.read(); }
  if (servoNum== 2) {  curAngle = myservo2.read(); }
  if (servoNum== 3) {  curAngle = myservo3.read(); }
  if (servoNum== 4) {  curAngle = myservo4.read(); }
  if (curAngle < newAngle) {
   for(int angle=curAngle;angle < newAngle;angle += angleInc) {
         if (servoNum == 1) myservo1.write(angle);
         if (servoNum == 2) myservo2.write(angle);
         if (servoNum == 3) myservo3.write(angle);
         if (servoNum == 4) myservo4.write(angle);
         delay(incDelay);   }
   }
   else if (curAngle > newAngle) {
      for(int angle=curAngle;angle > newAngle;angle -= angleInc) {
        if (servoNum == 1) myservo1.write(angle);
        if (servoNum == 2) myservo2.write(angle);
        if (servoNum == 3) myservo3.write(angle);
        if (servoNum == 4) myservo4.write(angle);
        delay(incDelay);   }
   }
   }
int readTilt() {
  int gyroVal  = analogRead(gyroPin);
  gyroVal  = map(gyroVal, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  delay(10);
  Serial.print(" front : ");Serial.println(gyroVal); 
  return(gyroVal);
} // end readTilt()

int readTilt2() { // sideTilt
  int gyroVal2 = analogRead(gyroPin2);
  gyroVal2 = map(gyroVal2, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  delay(10);
  Serial.print(" side : ");Serial.println(gyroVal2);
  return(gyroVal2);
} // end readTilt()
void setup()
{
    Serial.begin(9600);
    delay(100);
    myservo1.attach(3);  // attaches the servo on pin 3 to the servo object
    myservo1.write(90);
    delay(500);                           // waits for the servo to get there 
    myservo2.attach(5);  // attaches the servo on pin 5 to the servo object
    myservo2.write(90);                  // sets the servo position according to the scaled value 
    myservo3.attach(7);  // attaches the servo on pin 5 to the servo object
    myservo3.write(90);                  // sets the servo position according to the scaled value 
    myservo4.attach(9);  // attaches the servo on pin 5 to the servo object
    myservo4.write(90);                  // sets the servo position according to the scaled value 
    delay(500);                           // waits for the servo to get there
    delay(1000);                           // waits for the servo to get there 
    if (lowBoy) {  fRServo = 90; fLServo = 90; rRServo = 90;  rLServo = 90;
      myServo(0,1,5,1);myServo(0,1,5,2);myServo(0,1,5,3);myServo(0,1,5,4); delay(5000);}
    else { fRServo = 10; fLServo = 10; rRServo = 10;  rLServo = 10;}
    //////////////////////////////////////////////////////////////////
    // wheel servo order:       right front is 1
    //                          left  front is 2
    //                          left  rear  is 3
    //                          right rear  is 4
    //////////////////////////////////////////////////////////////////
}

void loop() {
  frontTilt = readTilt();
  sideTilt  = readTilt2();

if (frontTilt > 85 && sideTilt < 90) {
   // front right is lowest point
   if ( rLServo < 110) { // lower opposite wheelheight
    rLServo = rLServo + 2;
    myServo(rLServo,1,5,3);
   }
   if ( rLServo >= 110 && fLServo > 0) { // raise downward wheel
    fRServo = fRServo - 2;
     myServo(fRServo,1,5,1); }
}

 if (frontTilt < 85 && sideTilt > 90) {
   // rear left is lowest point
   //Serial.print(" fRServo : ");Serial.println(fRServo);
   if ( fRServo < 110) { // lower opposite wheel height
    fRServo = fRServo + 2;
    myServo(fRServo,1,5,1);
   }
   if ( rLServo >= 0 && fRServo >= 110) { // raise downward wheel height
    rLServo = rLServo - 2;
     myServo(rLServo,1,5,3); }
}
if (frontTilt > 85 && sideTilt > 90) {
   // front left is lowest point
   if ( rRServo < 110) { // lower opposite wheel
    rRServo = rRServo + 2;
    myServo(rRServo,1,5,4);
   }
   if ( rRServo >= 110 && fRServo > 0) { // raise downward wheel height
    fLServo = fLServo - 2;
     myServo(fLServo,1,5,2); }
}
if (frontTilt < 85 && sideTilt < 90) {
   // rear right is lowest point
   //Serial.print(" fRServo : ");Serial.println(fRServo);
   if ( fLServo < 110) { // lower opposite wheel
    fLServo = fLServo + 2;
    myServo(fLServo,1,5,2);
   }
   if ( rRServo >= 0 && fLServo >= 110) { // raise downward wheel height
    rRServo = rRServo - 2;
     myServo(rRServo,1,5,4); }
}
 //   exit(0); //pause program - hit reset to continue
}
