#importacion de modulos
from time import sleep
from rpi_TM1638 import TMBoards #imprtante cambio de biblioteca/modulo de TM1638 a rpi_TM1638
import random

#numeros de piens a usar en BCM para TMBoards
DIO = 19
CLK = 13
STB = 26
#intanciacion en TMBoards se incia los pin desabilitados con 0
TM = TMBoards(DIO, CLK, STB, 0)

#metodo limpieza de display similiar a clear.py
TM.clearDisplay()

print("Press Ctrl+C to finish")
#try except equivalente de try catch el C
try:
    while True:#ciclo infinito
        TM.leds[0] = bool(random.getrandbits(1))#prpiedad para el uso de leds se necita especifcar poscion 0-7 y estado por en tipo bool
        TM.leds[1] = bool(random.getrandbits(1))
        TM.leds[2] = bool(random.getrandbits(1))
        TM.leds[3] = bool(random.getrandbits(1))
        TM.leds[4] = bool(random.getrandbits(1))
        TM.leds[5] = bool(random.getrandbits(1))
        TM.leds[6] = bool(random.getrandbits(1))
        TM.leds[7] = bool(random.getrandbits(1))
        TM.segments[0] = str(random.randint(0,9))#propiedad de uso para s7 egmentos se especifa la posicion 0-7 asignacion en tipo string
        TM.segments[1] = str(random.randint(0,9))
        TM.segments[2] = str(random.randint(0,9))
        TM.segments[3] = str(random.randint(0,9))
        TM.segments[4] = str(random.randint(0,9))
        TM.segments[5] = str(random.randint(0,9))
        TM.segments[6] = str(random.randint(0,9))
        TM.segments[7] = str(random.randint(0,9))
        sleep(0.25)#visualizacion
        #random.getrandbits() y random.randint() generan bit y numeros en un rango respectivamente
        
except KeyboardInterrupt:#interrupcion por ctrl+C
    pass
#regreso a condicones iniciales
TM.leds[1] = False       
TM.leds[3] = False
TM.leds[5] = False
TM.leds[7] = False

TM.leds[0] = False       
TM.leds[2] = False
TM.leds[4] = False
TM.leds[6] = False
TM.clearDisplay()
#apatir de este codigo se obvian las imprtaciones e instaciacion 
