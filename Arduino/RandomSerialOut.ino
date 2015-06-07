
int n;
void setup()  
{
  n=0;
  Serial.begin(9600);

  // set the data rate for the SoftwareSerial port
 // mySerial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() // run over and over
{   
    int t = random(0,40);
    Serial.println(t);
    delay(1000);
    n++;
    //Sending command to python script simply to terminate after 10 readings
    if(n==10)
    {
      n=0;
      Serial.println("exit");
    }
}
