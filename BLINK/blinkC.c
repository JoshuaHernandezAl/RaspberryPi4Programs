#include <wiringPi.h>
int main (void){
	wiringPiSetupGpio();
	pinMode(21,OUTPUT);
	while(1){
		digitalWrite(21,HIGH);
		delay(500);
		digitalWrite(21,LOW);
		delay(500);
	}
	return 0;
}
