String msg;
const int bottom_rotate1 = 2 ;
const int bottom_rotate2 = 3 ;
const int middle_right1 = 4 ;
const int middle_right2 = 5 ;
const int middle_left1 = 6 ;
const int middle_left2 = 7 ;
const int top1 = 8 ;
const int top2 = 9;
 

void setup() {
  Serial.begin(9600);
  pinMode(top1, OUTPUT);
  pinMode(top2, OUTPUT);
  pinMode(bottom_rotate1,OUTPUT);
  pinMode(bottom_rotate2, OUTPUT);
  pinMode(middle_right1, OUTPUT);
  pinMode(middle_right2, OUTPUT);
  pinMode(middle_left1, OUTPUT);
  pinMode(middle_left2, OUTPUT);
}



void readSerialPort() {
  msg = "";;
    if (Serial.available() > 0) {
      msg = Serial.readStringUntil('\n');
    }
    Serial.print("Rotated!");
  }



void rotate_right(){
  digitalWrite(bottom_rotate1, HIGH);
  digitalWrite(bottom_rotate2, LOW);
}

void rotate_left(){
  digitalWrite(bottom_rotate2, HIGH);
  digitalWrite(bottom_rotate1, LOW);
  digitalWrite(LED_BUILTIN, LOW);
}

void bend_left(){
  digitalWrite(bottom_rotate2, HIGH);
  digitalWrite(bottom_rotate1, LOW);
}

void errorData() {
  //write data
  Serial.print("Some error occured!");
}



void loop() {
  readSerialPort();

  if (msg = "rot1") {
    void rotate_left();
    msg="";
    Serial.print("Rotated!");
  }
  else if (msg="rot2"){
    void rotate_right();
    Serial.print("Rotated!");
    msg="";
    
  }
  else{
    
    msg="";
    }
  delay(500);
  msg = "";
}
