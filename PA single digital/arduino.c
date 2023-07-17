
int serialdata;               //serial iletişimden aldimiz değeri tanıtıyoruz
int ledpin = 12;              //12 yerine karışmasın diye ledpin yazıyoruz
                   

//
void setup() {                    //setup işte
 pinMode(ledpin,OUTPUT);         //pini çıkış olarak gösteriyoruz
 Serial.begin(9600);             //haberleşmeyi 9600 ile başlatıyoruz
}

void loop() {                   // loop başgancı
 if(Serial.available()>0) {     // serial dan değer alıyorsa
  serialdata=Serial.read();     //bu değeri serialdata ya atıyoruz

  Serial.print("alindi :");    // alindi yazdırıyoruz ama serial monitor acilmiyor  
  Serial.println(serialdata);  // degeri yazdırıyoruz ama serial monitor acilmiyor
  if(serialdata=='1'){         // eğer gelen değer bir ise
    Serial.println("LED : ON "); //ledi yandığını yazdır
    digitalWrite(ledpin,HIGH);   //ledi yak
  }
  if(serialdata=='0'){            // eğer değer 0 ise
    Serial.println("LED : OFF "); //led off yazdırıyoruz
    digitalWrite(ledpin,LOW);    // ledi kapatıyoruz
 }
  
  }
}
