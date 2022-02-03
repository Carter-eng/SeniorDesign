#include <Arduino.h>
#define LED 13
int analogPin = A3;

int val = 0;

//int threshold = 0;

void setup() {
  //pinMode(LED, OUTPUT);
  Serial.begin(9600)

}

void loop() {
  val = analogRead(analogPin)
  Serial.println(val);
  //Uncomment the code below when value is found for threshold
  /*******************
  if (val >= threshold) {
    digitalWrite(LED,HIGH)
  }
  if (val < threshold) {
    digitalWrite(LED,LOW)
  }
   
   */

}
