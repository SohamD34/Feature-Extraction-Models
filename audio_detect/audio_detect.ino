#define MIC A0

int sig = 0;

void setup() {
 pinMode(2, OUTPUT);
 pinMode(3, OUTPUT);
 pinMode(4, OUTPUT);
 pinMode(5, OUTPUT);
}

void led() {
 sig = analogRead(MIC);

 Serial.println(sig); // print microphone value to serial monitor

 if (sig>1000)  {digitalWrite(2, HIGH);} else {digitalWrite(2, LOW);}
 if (sig>300) {digitalWrite(3, HIGH);} else {digitalWrite(3, LOW);}
 if (sig>800) {digitalWrite(4, HIGH);} else {digitalWrite(4, LOW);}
 if (sig>950) {digitalWrite(5, HIGH);} else {digitalWrite(5, LOW);}
}

void loop() {
 led();
}
