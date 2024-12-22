
void setup()
{
  pinMode(7, OUTPUT);
}

void loop()
{
  digitalWrite(7, HIGH);
  delay(5000); // Wait for 5000 millisecond(s)
  digitalWrite(7, LOW);
  delay(5000); // Wait for 5000 millisecond(s)
}
