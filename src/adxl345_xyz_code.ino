// How to use ADXL345 Accelerometer Sensor
// www.scitiver.com
// Created by : ScitiveR
// Date : 24.march.2020

#include <Wire.h>

int ADXL345 = 0x53;
int X_out, Y_out, Z_out;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  Wire.beginTransmission(ADXL345);
  Wire.write(0x2D); //talk to POWER_CTL Register - 0x2D
  
  Wire.write(8); // Bit D3 High for measuring enable (8dec -> 0000 1000 binary)
  Wire.endTransmission();
  delay(10);
}

void loop() {
  Wire.beginTransmission(ADXL345);
  Wire.write(0x32);
  Wire.endTransmission(false);
  Wire.requestFrom(ADXL345, 6, true);

  X_out = ( analogRead(A3));
  Y_out = ( analogRead(A2));
  Z_out = ( analogRead(A1));

  Serial.print(X_out);
  Serial.print(" ");
  Serial.print(Y_out);
  Serial.print(" ");
  Serial.println(Z_out);
  delay(100);
}















//c = map(X_out,-100,100,0,500);
