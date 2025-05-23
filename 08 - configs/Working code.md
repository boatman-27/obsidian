```cPP
#include <Arduino.h>

#include <DHT.h>

  

#if defined(ESP8266)

#include <ESP8266WiFi.h>

#endif

  

#include <ESP_Mail_Client.h>

  

// ==== WiFi + Email Config ====

#define WIFI_SSID "ARFA-LAPTOP 7306"

#define WIFI_PASSWORD "381x4<1T"

#define SMTP_HOST "smtp.gmail.com"

#define SMTP_PORT 465

#define AUTHOR_EMAIL "adham4603@gmail.com"

#define AUTHOR_PASSWORD "epgu bvvo skva whef"

#define RECIPIENT_EMAIL "adham.osman@gutech.edu.om"

  

// ==== Sensor Pins ====

#define DHTPIN D3

#define MOTION_PIN D4

#define SOUND_PIN D6

#define DHTTYPE DHT11

  

DHT dht(DHTPIN, DHTTYPE);

SMTPSession smtp;

  

void setup() {

Serial.begin(115200);

  

// === Connect to Wi-Fi ===

WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

Serial.print("Connecting to Wi-Fi");

while (WiFi.status() != WL_CONNECTED) {

delay(500);

Serial.print(".");

}

Serial.println("\nConnected! IP address: ");

Serial.println(WiFi.localIP());

  

// === Initialize Sensors ===

dht.begin();

delay(2000); // DHT warm-up time

pinMode(MOTION_PIN, INPUT);

pinMode(SOUND_PIN, INPUT);

  

// === Read Sensors with Retry ===

float temp = NAN;

float hum = NAN;

  

for (int i = 0; i < 5; i++) {

temp = dht.readTemperature();

hum = dht.readHumidity();

if (!isnan(temp) && !isnan(hum)) break;

delay(1000);

}

  

bool motion = digitalRead(MOTION_PIN);

bool sound = digitalRead(SOUND_PIN);

  

Serial.print("Temp: "); Serial.println(temp);

Serial.print("Humidity: "); Serial.println(hum);

Serial.print("Motion: "); Serial.println(motion ? "Yes" : "No");

Serial.print("Sound: "); Serial.println(sound ? "Yes" : "No");

  

// === Prepare Email ===

MailClient.networkReconnect(true);

Session_Config config;

config.server.host_name = SMTP_HOST;

config.server.port = SMTP_PORT;

config.login.email = AUTHOR_EMAIL;

config.login.password = AUTHOR_PASSWORD;

config.time.ntp_server = F("pool.ntp.org,time.nist.gov");

config.time.gmt_offset = 3;

config.time.day_light_offset = 0;

  

SMTP_Message message;

message.sender.name = F("ESP8266");

message.sender.email = AUTHOR_EMAIL;

message.subject = F("ESP8266 Sensor Report");

message.addRecipient(F("Adham"), RECIPIENT_EMAIL);

  

String content = "Temperature: " + String(temp) + " °C\n" +

"Humidity: " + String(hum) + " %\n" +

"Motion Detected: " + String(motion ? "Yes" : "No") + "\n" +

"Sound Detected: " + String(sound ? "Yes" : "No");

  

message.text.content = content.c_str();

message.text.charSet = "us-ascii";

message.text.transfer_encoding = Content_Transfer_Encoding::enc_7bit;

message.priority = esp_mail_smtp_priority::esp_mail_smtp_priority_low;

  

// === Send Email ===

if (smtp.connect(&config)) {

if (!MailClient.sendMail(&smtp, &message)) {

Serial.println("❌ Failed to send email:");

Serial.println(smtp.errorReason());

} else {

Serial.println("✅ Email sent successfully!");

}

} else {

Serial.println("❌ Could not connect to SMTP server.");

Serial.println(smtp.errorReason());

}

}

  

void loop() {

// No repeated logic needed here

}
```