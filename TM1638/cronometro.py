from rpi_TM1638 import TMBoards
from time import sleep
import sys

DIO = 19
CLK = 13
STB = 26
TM = TMBoards(DIO, CLK, STB, 0)

TM.clearDisplay()
s=0
m=0
h=0 
try:
      while True:#ciclo infinito
            TM.segments[2]='.'#despligue en 7 segmentos
            TM.segments[5]='.'
            TM.segments[3]='{:02d}'.format(abs(m))#dar formato a dos decimales con .format de modo que se depligue 00.00.00
            TM.segments[6]='{:02d}'.format(abs(s))
            TM.segments[0]='{:02d}'.format(abs(h))
            s+=1
            if s ==5:#para proposito de prueba 5 seg hacen un minuto 2 min hacen una hora
                  s=0
                  m+=1
                  if m==2:
                        seg=0
                        m=0
                        h+=1
                        if h==2:
                              TM.clearDisplay()
                              TM.segments[0]='Adios'
                              sleep(1)
                              TM.clearDisplay()
                              sys.exit()#llamada al sistema para forzar termino
            sleep(0.5)
except KeyboardInterrupt:
      pass
TM.clearDisplay()
      
