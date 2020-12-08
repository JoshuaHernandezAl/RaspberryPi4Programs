from time import sleep
from rpi_TM1638 import TMBoards
#pin en BCM
#IMPORTANTE YA QUE SE VA A RECIRBIR INFORMACION DEL MODULO ES NECESARIO CONECTAR A 3.3V 
STB = 14
CLK = 15
DIO = 18

TM = TMBoards(DIO, CLK, STB, 0)
TM.clearDisplay()

#variable de despligue en 7 seg controlada por botones
num_left = 0

TM.segments[0] = '0' #valor inicial

while True:#ciclo infinito aguarda la pulsacion de un boton
    if TM.switches[0]:#propiedad para acceder a los botones
        TM.leds[0]=True#uso de led
        sleep(0.25)#timepo para visualizar y operacion correcta 
        TM.leds[0]=False
        if num_left > 0: #resta de unidad y despligue en display, no tabaja para nuemeros negativos
                num_left -= 1
                TM.clearDisplay()
                TM.segments[0]=str(num_left)
    if TM.switches[1]:#incremento de unidad y despligue en display
        TM.leds[1]=True
        sleep(0.25)
        TM.leds[1]=False
        num_left += 1
        TM.clearDisplay()
        TM.segments[0]=str(num_left)
    if TM.switches[2]:#reset  a cero
            TM.leds[2]=True
            sleep(0.25)
            TM.leds[2]=False 
            num_left = 0
            TM.clearDisplay()
            TM.segments[0]='0'
    if TM.switches[3]:#salida del programa
        TM.clearDisplay()
        break
    
    
