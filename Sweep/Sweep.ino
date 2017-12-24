/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo servoLeft;          // 宣告左邊伺服馬達
Servo servoRight;         // 宣告右邊伺服馬達

int pos = 0;    // variable to store the servo position

void setup() { 
  servoLeft.attach(10);  // 將 Pin 10 指定為左邊伺服馬達
  servoRight.attach(9);  // 將 Pin  9 指定為右邊伺服馬達
  Serial.begin(9600);
} 

void loop() {
  dance();
}

void dance() {
  for (pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servoLeft.write(pos);              // tell servo to go to position in variable 'pos'
    servoRight.write(pos);              // tell servo to go to position in variable 'pos'
    delay(5);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 90; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    servoLeft.write(pos);              // tell servo to go to position in variable 'pos'
    servoRight.write(pos);              // tell servo to go to position in variable 'pos'
    delay(5);                       // waits 15ms for the servo to reach the position
  }
}

void freeze(){
    servoLeft.write(0);              
    servoRight.write(0);  
}

