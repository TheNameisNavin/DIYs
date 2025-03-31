void setup()
{
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
}

void loop()
{
  digitalWrite(8, HIGH);
  delay(2000); // Wait for 2000 millisecond(s)
  digitalWrite(8, LOW);
  delay(3000); // Wait for 3000 millisecond(s)
  digitalWrite(7, HIGH);
  delay(5000); // Wait for 5000 millisecond(s)
  digitalWrite(7, LOW);
  delay(5000); // Wait for 5000 millisecond(s)
}



