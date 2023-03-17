//RASPBERRY PI CODE

import serial // pyserial library
import requests

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Set up the serial communication with ESP
url = "http://esp_ip_address/data"  # Set up the ESP's endpoint for receiving data

while True:
    data = ser.readline().decode().strip()  # Read serial data from Raspberry Pi
    requests.post(url, data=data)  # Send the data to ESP over WiFi




// ESP CODE C++

#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>

const char* ssid = "your_wifi_ssid";
const char* password = "your_wifi_password";
const char* arduino_port = "/dev/ttyS0"; // Set up the serial port of your Arduino
const int baud_rate = 9600; // Set up the baud rate of your Arduino

AsyncWebServer server(80);
HardwareSerial SerialToArduino(1); // Use UART1 for communicating with Arduino

void setup() {
  Serial.begin(115200);
  SerialToArduino.begin(baud_rate, SERIAL_8N1, 17, 16); // Set up the serial communication with Arduino
  WiFi.begin(ssid, password); // Connect to WiFi
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("WiFi connected");
  server.on("/data", HTTP_POST, handleData); // Set up the endpoint for receiving data from Raspberry Pi
  server.begin();
}

void loop() {
  // Nothing to do here
}

void handleData(AsyncWebServerRequest *request) {
  String data = request->getParam("plain")->value(); // Get the data from Raspberry Pi
  SerialToArduino.print(data); // Send the data to Arduino over serial
}
