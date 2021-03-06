// Example testing sketch for various DHT humidity/temperature sensors
// Written by ladyada, public domain

#include "DHT.h"
//#include<DateTime.h>
//#include<DateTime.h>
//#include<SPI.h>
//import processing.serial.*;
#define DHTPIN 9     // what digital pin we're connected to
#define ledPin 13
//Suv#include<ThingSpeak.h>
//Suv#include<WifiClient.h>
// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)
DHT dht(DHTPIN, DHTTYPE);
// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.

//PrintWriter output;
//char auth[] = "f50e77a26c53496fa7b1f11b2c909f46";

// Your WiFi credentials.
// Set password to "" for open networks.
//Suvchar ssid[] = "AndroidAP";
//Suvchar pass[] = "kashmira";
//SuvWifiClient client;
//Suvunsigned long myChannel1Number = 590512;
//Suvconst char = myWriteApiKey= 'RXNCVXI31I2ZAVET'
const int analogInPin1 = A0;
const int analogInPin2 = A1;
int sensorValue1 = 0;
int sensorValue2 = 0;
uint8_t temperature,humidity;
void setup() {
  Serial.begin(115200);
  dht.begin();
 // Serial.println("DHTxx test!");
  pinMode(ledPin,OUTPUT);
  //dht.begin();
  //dht.getMinimumSamplingPeriod();
  //output=createWriter("output_file.txt");
}

void loop() {
  // Wait a few seconds between measurements.
  delay(60000);
  //delay(dht.getminimumsamplingperiod());
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);
  sensorValue1 = analogRead(analogInPin1);
  sensorValue2 = analogRead(analogInPin2);
  
  Serial.print("Ammonia:");
  Serial.print(sensorValue1);
  Serial.print(",");
  Serial.print("Smoke:");
  Serial.print(sensorValue2);
  Serial.print(",");
  Serial.print("Humidity:");
  Serial.print(h);
  Serial.print(",");
  Serial.print("Temperature:");
  Serial.print(t);
  //time_t ti = now();
  //Serial.print(hour(ti));
  //output.print("Ammonia:");
  //output.print(sensorValue1);
  //output.print(",");
  //output.print("Smoke:");
  //output.print(sensorValue2);
  //output.print(",");
  //output.print("Humidity:");
  //output.print(h);
  //output.print(",");
  //output.print("Temperature:");
  //output.print(t);
  //Serial.print(" *C ");
  //Serial.print(f);
  //Serial.print(" *F\t");
  //Serial.print("Heat index: ");
  //Serial.print(hic);
  //Serial.print(" *C ");
  //Serial.print(hif);
  Serial.println();
  //output.println();
  //output.flush();
  if(h>70){
    digitalWrite(ledPin,HIGH);
  }
  else {
    digitalWrite(ledPin,LOW);
  }
}
