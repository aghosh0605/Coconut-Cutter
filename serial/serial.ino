String msg;

void setup() {
  Serial.begin(9600);
}

void loop() {
  readSerialPort();

  if (msg = "") {
    
  }
  else if (msg=""){
    
  }
  else{
    errorData();
    }
  delay(500);
  msg = "";
}

void readSerialPort() {
  msg = "";
  if (Serial.available()) {
    delay(10);
    while (Serial.available() > 0) {
      msg += (char)Serial.read();
    }
    Serial.flush();
  }
}

void errorData() {
  //write data
  Serial.print("Some error occured!");
}
