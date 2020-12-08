#include <iostream>
#include <wiringPi.h>
using namespace std;
int ledPin=29;
void setup(){
	pinMode(ledPin,OUTPUT);
}

void loop(){
	digitalWrite(ledPin,HIGH);
	delay(500);
	digitalWrite(ledPin,LOW);
	delay(500);
}
int main(void){
	if(wiringPiSetup()<0){
		cout<<"setup wiring pi failed"<<endl;
		return 1;
	}
	setup();
	while(1){
		loop();
	}
	return 0;
}
