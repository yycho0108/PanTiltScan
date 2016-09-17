/*
  Blink
 Turns on an LED on for one second, then off for one second, repeatedly.
 
 This example code is in the public domain.
 */

// Pin 13 has an LED connected on most Arduino boards.
// Pin 11 has the LED on Teensy 2.0
// Pin 6  has the LED on Teensy++ 2.0
// Pin 13 has the LED on Teensy 3.0
// give it a name:

#define M_PI 3.14159265358979

float delta = 5, theta = 0, phi = 0;

// the setup routine runs once when you press reset:
void setup() {                
    Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
    theta += 0.74;
    phi += 1.13;
    Serial.print(delta);
    Serial.print(',');
    Serial.print(d2r(theta));
    Serial.print(',');
    Serial.println(d2r(phi));
    //delay(10);
}
