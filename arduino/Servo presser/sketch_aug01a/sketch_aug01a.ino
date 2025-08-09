#include <Servo.h>

Servo myservo;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
}

char serialData = '1';
char oldData = serialData;

void loop() {
  if (Serial.available() > 0) {
    serialData = Serial.read();
  }
  
  if (oldData != serialData)
    if (serialData == '1')
      myservo.write(40);
    else
      myservo.write(180);    
  oldData = serialData;

//  myservo.write(40);
//  delay(1500);
//  myservo.write(180);
//  delay(1500);
}
