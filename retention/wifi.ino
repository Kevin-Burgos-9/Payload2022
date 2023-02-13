#include <WiFiEsp.h>

// Replace with your network credentials
const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

// IP address of the device to send messages to
IPAddress deviceIp(192, 168, 1, 2);
int port = 80;

// Create an instance of the WiFiClient class
WiFiEspClient client;

void setup() {
  // initialize serial communication
  Serial.begin(115200);
  
  // initialize ESP module
  WiFi.init(&Serial);
  
  // check for the presence of the shield
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("WiFi shield not present");
    while (true);
  }
  
  // Connect to the network
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print("Connecting to WiFi network: ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);
    delay(5000);
  }
  Serial.println("Connected to WiFi network");
}

void loop() {
  // Connect to the device
  if (client.connect(deviceIp, port)) {
    // Send a message
    client.println("Hello from ESP01!");
    client.flush();
    client.stop();
    Serial.println("Message sent");
  }
  else {
    Serial.println("Connection failed");
  }
  
  // Wait for some time before sending the next message
  delay(5000);
}
