from rpi_TM1638 import TMBoards
from time import sleep

DIO = 19
CLK = 13
STB = 26
TM = TMBoards(DIO, CLK, STB, 0)

TM.clearDisplay()
s=int(input("Ingresa sengudos para el temporizador: "))
m=int(input("Ingresa minutos para el temporizador: "))
h=int(input("Ingresa horas para el temporizador: "))
while True:
      if h==0 and m<0 and s==2:
            h=0
            m=0
            s=0
            TM.segments[0]='00'
            TM.segments[2]='.'
            TM.segments[3]='00'
            TM.segments[5]='.'
            TM.segments[6]='00'
            break
      TM.segments[0]='{:2d}'.format(abs(h))
      TM.segments[2]='.'
      TM.segments[3]='{:2d}'.format(abs(m))
      TM.segments[5]='.'
      TM.segments[6]='{:2d}'.format(abs(s))
      s-=1
      if h!=0:
            if s==0:
                  s=2
                  m-=1
                  if m==0:
                        m=2
                        h-=1
      elif h==0:
            if s==0:
                  s=2
                  m-=1
      sleep(1)
  
TM.clearDisplay()
TM.leds[0]=True
TM.leds[1]=True
TM.leds[2]=True
TM.leds[3]=True
TM.leds[4]=True
TM.leds[5]=True
TM.leds[6]=True
TM.leds[7]=True
TM.segments[0]='Kaboom'
sleep(2)
TM.clearDisplay()
TM.leds[0]=False
TM.leds[1]=False
TM.leds[2]=False
TM.leds[3]=False
TM.leds[4]=False
TM.leds[5]=False
TM.leds[6]=False
TM.leds[7]=False
