import lcddriver
from time import sleep

lcd=lcddriver.lcd()

a=input("ingresa una cadena: ")
i=0
j=0
if len(a)<=16:
	lcd.lcd_display_string(a,1)
	sleep(1)
	lcd.lcd_clear()
else:
	b=a.split()
	while i<len(b)-1:
		l1=len(b[j])
		if j+1<len(b):
			l2=len(b[j+1])
		if l1+l2+1<=16:
			if j+1<len(b):
				aux=b[j]+' '+b[j+1]
				lcd.lcd_display_string(aux,1)
			else: 
				aux= b[j]
				lcd.lcd_display_string(aux,1)
		elif l1+l2+1>16:
			aux=b[j]
			if j+1 < len(b):
				aux2=b[j+1]
				lcd.lcd_display_string(aux,1)
				lcd.lcd_display_string(aux2,2)
			else:
				lcd.lcd_display_string(aux,1)
		sleep(1)
		lcd.lcd_clear()
		i+=1
		j=i+1
			

lcd.lcd_backlight(0)
