#include <Servo.h> 

#define M_PI 3.14159265358979

Servo yaw_servo;
Servo pitch_servo;

const int IR_PIN = A0;


float d2r(float d){
    return d * M_PI / 180;
}

float r2d(float r){
    return r * 180 / M_PI;   
}

float delta=0, phi=d2r(0), theta=0;

//delta in volts

//phi,theta in radians


void setup() 
{
    Serial.begin(9600);
    Serial.setTimeout(1000); //max 1 sec
    
    pinMode(2, INPUT_PULLUP);
    pinMode(IR_PIN, INPUT);
    yaw_servo.attach(5);
    pitch_servo.attach(6);
}

void loop() 
{ 
    delta = 5 * analogRead(IR_PIN) / 1023.0;
    
    // debug
    //Serial.print(phi);
    //Serial.print(',');
    //Serial.print(theta);
    //Serial.print(',');
    Serial.println(delta);

    if(Serial.available()){
        theta = Serial.read();
        phi = Serial.read();
        Serial.flush();
        //theta = Serial.parseFloat();
        //phi = Serial.parseFloat();
        //if(phi > 0 && theta > 0){
            yaw_servo.write(theta);
            pitch_servo.write(phi);    
        //}

    }

}

