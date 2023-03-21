#include <SoftwareSerial.h>

SoftwareSerial espSerial(0, 1); // RX, TX pins for ESP01
String ssid = "MyESPAP"; // Set the access point name
String password = "password"; // Set the access point password

void setup() {
  Serial.begin(9600);
  espSerial.begin(9600);
  
  espSerial.println("AT+RST"); // Reset the ESP01
  delay(1000);
  
  espSerial.println("AT+CWMODE=2"); // Set the ESP01 to access point mode
  delay(1000);
  
  String cmd = "AT+CWSAP=\"";
  cmd += ssid;
  cmd += "\",\"";
  cmd += password;
  cmd += "\",5,3";
  espSerial.println(cmd); // Set the access point SSID and password
  delay(1000);
  
  espSerial.println("AT+CIFSR"); // Get the IP address of the access point
  delay(1000);
  
  espSerial.println("AT+CIPMUX=1"); // Set up the ESP01 to allow multiple connections
  delay(1000);
  
  espSerial.println("AT+CIPSERVER=1,80"); // Start the server on port 80
  delay(1000);
  
  Serial.println("Access point set up.");
}

void loop() {
  if (espSerial.available()) {
    String request = espSerial.readStringUntil('\n');
    Serial.println(request);
    
    String response = "HTTP/1.1 200 OK\r\n";
    response += "Content-Type: text/html\r\n\r\n";
    response += "<!DOCTYPE HTML>\r\n";
    response += "<html>\r\n";
    response += "<h1>Hello from ESP01</h1>\r\n";
    response += "</html>\r\n";
    espSerial.println("AT+CIPSEND=0," + String(response.length()));
    delay(10);
    espSerial.print(response);
    delay(10);
    espSerial.println("AT+CIPCLOSE=0");
    delay(1000);
  }
}
