import lcddriver
import time


display = lcddriver.lcd()
try:
    print("Ctrl + C termino")
    display.lcd_display_string("Hora:", 1) 
    display.lcd_display_string("Fecha:",2)
    while True:
        display.lcd_display_string(time.strftime("%x"),1)
        display.lcd_display_string(time.strftime("%I:%M:%S"),2)

except KeyboardInterrupt:
    display.lcd_clear()
    display.lcd_backlight(0)
