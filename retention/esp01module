#include <ESP8266WiFi.h>
#include "DHT.h"

#define DHTPIN 2        // what digital pin we're connected to
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

const char* ssid     = "Circuits DIY"; // Your ssid
const char* password = "03433212601"; // Your Password
WiFiServer server(80);

void setup() {
  
// Start DHT11  
dht.begin();  
Serial.begin(115200);
delay(10);
Serial.println();

// Connect to WiFi network
WiFi.mode(WIFI_STA);
Serial.println();
Serial.println();
Serial.print("Connecting to ");
Serial.println(ssid);

WiFi.begin(ssid, password);

while (WiFi.status() != WL_CONNECTED) {
delay(500);
Serial.print(".");
}
Serial.println("");
Serial.println("WiFi connected");

// Start the server
server.begin();
Serial.println("Server started");

// Print the IP address
Serial.println(WiFi.localIP());
}

void loop() {

 float h = dht.readHumidity();
 float t = dht.readTemperature(); // Read temperature as Celsius (the default)
 float f = dht.readTemperature(true); // Read temperature as Fahrenheit (isFahrenheit = true)

 Check if any reads failed and exit early (to try again).
 if (isnan(h) || isnan(t) || isnan(f)) {
 Serial.println("Failed to read from DHT sensor!");
 return;
 }
   
 Serial.print("Humidity % : ");
 Serial.println(h);
 Serial.print("Temperature *C: ");
 Serial.println(t);
 Serial.print("Temperature *F: ");
 Serial.println(f);

WiFiClient client = server.available();
client.println("HTTP/1.1 200 OK");
client.println("Content-Type: text/html");
client.println("Connection: close");  // the connection will be closed after completion of the response
client.println("Refresh: 5");  // refresh the page automatically every 5 sec
client.println();
client.println("<!DOCTYPE html>");
client.println("<html xmlns='http://www.w3.org/1999/xhtml'>");
client.println("<head>\n<meta charset='UTF-8'>");
client.println("<title>ESP8266 Temperature & Humidity DHT11 Sensor</title>");
client.println("</head>\n<body>");
client.println("<H2>ESP8266 & DHT11 Sensor</H2>");
client.println("<H3>Humidity / Temperature</H3>");
client.println("<pre>");
client.print("Humidity (%)         : ");
client.println((float)h, 2);
client.print("Temperature (°C)  : ");
client.println((float)t, 2);
client.print("Temperature (°F)  : ");
client.println((float)f, 2);
//client.print("Temperature (°K)  : ");
//client.println(Kelvin(temp), 2);
client.println("</pre>");
client.println("<H3>www.Circuits-DIY.com</H3>");
client.print("</body>\n</html>");
delay(2000);
}
