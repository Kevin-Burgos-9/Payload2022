#include <ESP8266WiFi.h>
#include <WiFiClient.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* serverAddress = "RASPBERRY_PI_IP_ADDRESS";
const int serverPort = 1234;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  WiFiClient client;
  if (client.connect(serverAddress, serverPort)) {
    client.println("Hello from ESP-01");
    delay(1000);
  }
  else {
    Serial.println("Connection failed");
  }
}
