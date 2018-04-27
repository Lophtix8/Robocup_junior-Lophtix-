int trig[] = {2,4,6,14,4,18};
int echo[] = {3,5,7,15,17,19};
int enA = 10;
int enB = 11;
int Am1 = 9;
int Am2 = 8;
int Bm1 = 13;
int Bm2 = 12;
int Light = 16;

void setup() {
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(Am1, OUTPUT);
  pinMode(Am2, OUTPUT);
  pinMode(Bm1, OUTPUT);
  pinMode(Bm2, OUTPUT);
  for(int pin = 0; pin<6; pin++){
    pinMode(trig[pin], OUTPUT);
    pinMode(echo[pin], INPUT);
  }
  pinMode(Light, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()){
    int value = Serial.read();
    if (value == 48){//Forward
      digitalWrite(Am1, HIGH);
      digitalWrite(Am2, LOW);
      digitalWrite(Bm1, HIGH);
      digitalWrite(Bm2, LOW);
      analogWrite(enA, 100);
      analogWrite(enB, 100);
      delay(2000);
      digitalWrite(Am1, LOW);
      digitalWrite(Bm1, LOW);
      digitalWrite(enA, LOW);
      digitalWrite(enB, LOW);
    } else if(value == 49){//Backwards
      digitalWrite(Am1, LOW);
      digitalWrite(Am2, HIGH);
      digitalWrite(Bm1, LOW);
      digitalWrite(Bm2, HIGH);
      analogWrite(enA, 100);
      analogWrite(enB, 100);
      delay(2000);
      digitalWrite(Am2, LOW);
      digitalWrite(Bm2, LOW);
      digitalWrite(enA, LOW);
      digitalWrite(enB, LOW);
      
    } else if(value == 50){//TurnRight
    
    } else if(value == 51){//TurnLeft
    
    } else if(value == 52){//US
      for(int i=0;i<6;i++){
        int t = trig[i];
        int e = echo[i];
        digitalWrite(t, HIGH);
        delayMicroseconds(10);
        digitalWrite(t, LOW);
        int duration = pulseIn(e, HIGH);
        Serial.println(duration);
      } 
    }/* else if(value == 53){
      color = analogRead(Light);
      if (color < x){
        Serial.println(0);
      }  else if (color > y){
        Serial.println(1);
      }
    }*/
  }    
}
