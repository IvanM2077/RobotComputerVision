// Definición de pines
const int ledpin1 = 2; //conectando al pin para determinar la señal entrada. 
const int ledpin2 = 7; //conectando al pin para determinar la señal entrada. 
const int in1 = 3;  // Conectado al pin IN1 del L298N
const int in2 = 4;  // Conectado al pin IN2 del L298N
const int in3 = 5;  // Conectado al pin IN3 del L298N
const int in4 = 6;  // Conectado al pin IN4 del L298N



void setup() {
  // Configurar pines como salidas
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(ledpin1, OUTPUT);
  pinMode(ledpin2, OUTPUT);
  Serial.begin(9600);


}

void loop() {
  // Condicion para saber si se encuentra disponible el puerto serial. 
  if (Serial.available() > 0){
    char CaracterRecibido = Serial.read();

    if (CaracterRecibido == 'w'){
      digitalWrite(ledpin1, HIGH);//led indicador 
      
      Adelante();
      //si hay algún cambio en el puerto serial cambia el apaga el led y deten el motor
      if (CaracterRecibido != 'w'){
        delay(500);
        digitalWrite(ledpin1, LOW);
        //
        Stop();
        //
        digitalWrite(ledpin2, HIGH); //led indicador paro
        delay(300);
        digitalWrite(ledpin2, LOW);
      }
    }




    //Izquierda
    if (CaracterRecibido == 'a'){
      digitalWrite(ledpin1, HIGH);//led indicador
      
      Izquierda();
      //si hay algún cambio en el puerto serial cambia el apaga el led y deten el motor
      if (CaracterRecibido != 'w'){
        delay(500);
        digitalWrite(ledpin1, LOW);
        //
        Stop();
        //
        digitalWrite(ledpin2, HIGH);//led indicador paro
        delay(300);
        digitalWrite(ledpin2, LOW);
      }
    }



    //Derecha
    if (CaracterRecibido == 'd'){
      digitalWrite(ledpin1, HIGH);
      
      Derecha();
      //si hay algún cambio en el puerto serial cambia el apaga el led y deten el motor
      if (CaracterRecibido != 'w'){
        delay(500);
        digitalWrite(ledpin1, LOW);
        //
        Stop();
        //
        digitalWrite(ledpin2, HIGH);//led indicador paro
        delay(300);
        digitalWrite(ledpin2, LOW);
      }
    }
    



    //Atras
    if (CaracterRecibido == 's'){
      digitalWrite(ledpin1, HIGH);
      
      Adelante();
      //si hay algún cambio en el puerto serial cambia el apaga el led y deten el motor
      if (CaracterRecibido != 'w'){
        delay(500);
        digitalWrite(ledpin1, LOW);
        //
        Stop();
        //
        digitalWrite(ledpin2, HIGH);
        delay(300);
        digitalWrite(ledpin2, LOW);
      }
    }



  }

}


void Adelante(){
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}

void Atras(){
    // Atras
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);

  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
}

void Derecha(){

    // Detiene
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

}

void Izquierda(){
  
    // Detiene
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);

  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);

}


void Stop(){
  // Detiene
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);

  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

}
