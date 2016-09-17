#define NOT_AN_INTERRUPT -1

#include <Servo.h> 

Servo yaw_servo;
Servo roll_servo;

const int IR_PIN = A0;

void calib(){
   
}
void setup() 
{
    Serial.begin(9600);
    pinMode(IR_PIN, INPUT);
}

void loop() 
{ 
    float voltage = 5 * analogRead(IR_PIN) / 1023.;
    Serial.println(voltage);
    
}
