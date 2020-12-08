from rpi_TM1638 import TMBoards
import time

DIO = 19
CLK = 13
STB = 26
TM = TMBoards(DIO, CLK, STB, 0)

TM.clearDisplay()
try:
      while True:#ciclo infinito
            TM.segments[0]=time.strftime("%H")#uso de time para obtener el reloj del sistema
            TM.segments[2]='.'
            TM.segments[3]=time.strftime("%M")
            TM.segments[5]='.'
            TM.segments[6]=time.strftime("%S")
            time.sleep(1)
except KeyboardInterrupt:
      pass
TM.clearDisplay()
      
