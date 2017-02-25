int ledpin = 7;

void setup()
{
    // set up the Baud rate have it the same as python script
    Serial.begin(9600);
    // for testing purposes
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(ledpin, OUTPUT);
}

void loop()
{
    // going to read from serial
    char state = Serial.read();

    if (state == 'R') {
        digitalWrite(ledpin, HIGH);
        delay(1000);
    } else {
        digitalWrite(ledpin, LOW);
        delay(1000);
    }
}
