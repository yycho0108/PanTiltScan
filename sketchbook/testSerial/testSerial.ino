#include <ros.h>
#include <ros/msg.h>
#include <std_msgs/Int16.h>

enum dtype : 
uint8_t{
    Int16,
    Float32,
    String,
    Bool,
    Byte,
    Char,
};

struct msg_t{
    dtype t;
    char topic[3];
    char method[4];
    uint8_t buf[8];
};

void setup(){
    Serial.begin(9600);
}

void loop(){
    std_msgs::Int16 msg;
    msg.data = 65;
    msg_t buf = { 
        Int16,
        "to",
        "pub",    
    };
    msg.serialize(buf.buf);

    Serial.write((uint8_t*) &buf, sizeof(buf));
}
