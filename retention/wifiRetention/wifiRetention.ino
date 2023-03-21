#include <SoftwareSerial.h>

// Define the serial port settings
SoftwareSerial mySerial(2, 1);  // RX, TX pins of the software serial port
const int BAUD_RATE = 9600;

void setup() {
  // Open the software serial port
  Serial.begin(9600);
  mySerial.begin(9600);
  mySerial.println("AT+RST");
  // Open the Serial Monitor
  Serial.begin(9600);
}

void loop() {
  // Read data from the software serial port line by line
  while (mySerial.available()) {
    String line = mySerial.readStringUntil('\n');

    // Search for the "^_^" sequences in the line
    int firstIndex = line.indexOf("^_^");
    int secondIndex = line.indexOf("^_^", firstIndex + 1);

    if (firstIndex != -1 && secondIndex != -1) {
      // Extract the data between the "^_^" sequences
      String data = line.substring(firstIndex + 3, secondIndex);
      // Print the data
      Serial.println("Received data: " + data);
      // Stop searching for the sequences
      break;
    }
  }
}
