#include <Servo.h>

Servo servo1;  
Servo servo2;  
Servo servo3;  
Servo servo4;
Servo servo5;
void finger1(int pos);
void finger2(int pos);
void finger3(int pos);
void finger4(int pos);
void finger5(int pos);


void setup() {
  servo1.attach(5); 
  servo2.attach(6);  
  servo3.attach(9);  
  servo4.attach(10);  
  servo5.attach(11);  

  Serial.begin(9600);
  //char inp = 0;
}

void loop() {
  //servo3.write(135);
  
  while (Serial.available()) {
    char inp = Serial.read();
    Serial.println(inp);
    
    if (inp == 'g') {
      finger1(1);
    }
    if (inp == 'f') { 
      finger2(1);
    }
    if (inp == 'd') {
      finger3(1);
    }
    if (inp == 's') {
      finger4(1);
    }
    if (inp == 'a') {
      finger5(1);
    }
    
    if (inp == 't') {
      finger1(0);
    }
    if (inp == 'r') {
      finger2(0);
    }
    if (inp == 'e') {
      finger3(0);
    }
    if (inp == 'w') {
      finger4(0);
    }
    if (inp == 'q') {
      finger5(0);
    }
  }
}

void finger1(int pos) {
  if (pos == 0) {
    servo1.write(40);
  }
  else {
    servo1.write(150);
  }
}


void finger2(int pos) {
  if (pos == 0) {
    servo2.write(20);
  }
  else {
    servo2.write(150);
  }
}


void finger3(int pos) {
  if (pos == 0) {
    servo3.write(35);
  }
  else {
    servo3.write(150);
  }
}


void finger4(int pos) {
  if (pos == 0) {
    servo4.write(45);
  }
  else {
    servo4.write(160);
  }
}


void finger5(int pos) {
  if (pos == 0) {
    servo5.write(35);
  }
  else {
    servo5.write(150);
  }
}

