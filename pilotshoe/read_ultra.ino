#include <Servo.h>
#define TURN_TIME 175

Servo servo;
const int trigPin = 2;
const int echoPin = 4;
long duration, inches, cm;
int interval = -3;

long microsecondsToInches(long microseconds);
long microsecondsToCentimeters(long microseconds);

void setup() {
    Serial.begin(9600);
    servo.attach(10);
    servo.write(87);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop() {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    inches = microsecondsToInches(duration);
    cm = microsecondsToCentimeters(duration);

    Serial.print(inches);
    Serial.println();
    interval++;
    if (interval >= 3) {
        interval = -3;
    }
    if (interval < 0) {
        Serial.println("Switch low!");
        servo.write(89);
    } else {
        Serial.println("Switch high!");
        servo.write(98);
    }
    delay(100);
}

long microsecondsToInches(long microseconds) {
    return microseconds / 148;
}

long microsecondsToCentimeters(long microseconds) {
    return microseconds / 58;
}
