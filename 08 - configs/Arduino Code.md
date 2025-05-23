```cPP
// Include necessary libraries

#include <Wire.h>

#include <LiquidCrystal.h>

#include <DHT.h>

#include <ESP8266WiFi.h>

#include <WiFiClient.h>

#include <ESP8266WebServer.h>

  

#define SOUND_SENSOR_PIN A0 // Analog pin for sound sensor

#define DHT_PIN 14 // GPIO14 (D5)

#define PIR_PIN 12 // GPIO12 (D6)

#define LCD_RS 5 // GPIO5 (D1)

#define LCD_EN 4 // GPIO4 (D2)

#define LCD_D4 0 // GPIO0 (D3)

#define LCD_D5 2 // GPIO2 (D4)

#define LCD_D6 13 // GPIO13 (D7)

#define LCD_D7 15 // GPIO15 (D8)

  
  

// Define WiFi credentials

const char* ssid = "Mohammed's iPhone";

const char* password = "12345678";

  

// Define server IP and port

IPAddress serverIP(192, 168, 1, 100); // Change as needed

int serverPort = 80;

  

// Initialize objects

LiquidCrystal lcd(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

DHT dht(DHT_PIN, DHT11);

ESP8266WebServer server(80);

  

// Variables

unsigned long startTime = 0;

unsigned long sleepStart = 0;

unsigned long sleepTime = 0;

bool isSleeping = false;

int soundValue = 0;

int motionValue = 0;

float temperature = 0;

float humidity = 0;

  

void setup() {

Serial.begin(9600);

lcd.begin(16, 2);

lcd.print("Connecting WiFi");

  

WiFi.begin(ssid, password);

while (WiFi.status() != WL_CONNECTED) {

delay(500);

Serial.print(".");

lcd.print(".");

}

  

Serial.println("\nWiFi connected");

lcd.clear();

lcd.print("WiFi connected!");

  

// Start server and sensors

server.on("/", handleRoot);

server.begin();

Serial.println("Server started");

  

dht.begin();

pinMode(SOUND_SENSOR_PIN, INPUT);

pinMode(PIR_PIN, INPUT);

  

delay(2000);

lcd.clear();

lcd.print("Baby Monitor");

lcd.setCursor(0, 1);

lcd.print("Monitoring...");

}

  

void loop() {

motionValue = digitalRead(PIR_PIN);

soundValue = analogRead(SOUND_SENSOR_PIN);

  

if (motionValue == LOW && soundValue < 100) {

if (!isSleeping) {

sleepStart = millis();

isSleeping = true;

}

} else {

if (isSleeping) {

sleepTime += (millis() - sleepStart) / 1000;

isSleeping = false;

}

}

  

// Read temperature & humidity

temperature = dht.readTemperature();

humidity = dht.readHumidity();

  

// Display on LCD

lcd.clear();

lcd.setCursor(0, 0);

lcd.print("Temp:");

lcd.print(temperature);

lcd.print("C");

  

lcd.setCursor(0, 1);

lcd.print("Hum:");

lcd.print(humidity);

lcd.print("%");

  

sendSensorReadings();

server.handleClient();

delay(3000); // Delay for stability

}

  

void handleRoot() {

server.send(200, "text/plain", "Sleep Time: " + String(sleepTime) + "s");

sleepTime = 0;

}

  

void sendSensorReadings() {

WiFiClient client;

if (client.connect(serverIP, serverPort)) {

client.print("GET /?temp=");

client.print(temperature);

client.print("&humidity=");

client.print(humidity);

client.println(" HTTP/1.1");

client.println("Host: 192.168.1.100");

client.println("Connection: close");

client.println();

}

client.stop();

}
```