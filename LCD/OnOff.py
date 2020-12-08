import lcddriver
import time


display = lcddriver.lcd()
display.lcd_backlight(0)
try:
    print("Press CTRL + C to exit")
    display.lcd_backlight(1)
    while True:
        display.lcd_display_string("Hola!",1)
        time.sleep(0.5)
        display.lcd_display_string("Adios!",1)
        time.sleep(0.5)
        display.lcd_backlight(0)
        time.sleep(0.5)
        
except KeyboardInterrupt: 
    display.lcd_clear()
    display.lcd_backlight(0) 
