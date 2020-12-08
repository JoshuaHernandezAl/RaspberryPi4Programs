from time import sleep
from rpi_TM1638 import TMBoards
import math
import sys

STB = 14
CLK = 15
DIO = 18

TM = TMBoards(DIO, CLK, STB, 0)
TM.clearDisplay()
''' 
s0->+
s1-> -
s2-> *
s3-> /
s4-> raiz
s5-> potencia
s6-> borrar display
s7-> salir
'''
#menu de opciones
print("s0->+\ns1-> -\ns2-> *\ns3-> /\ns4-> raiz\ns5-> potencia\ns6-> borrar display\ns7-> salir")
num_left=0
TM.segments[0]='0'#valor inicial
while True:
    a=int(input("Ingresa a: "))#solicitud al usuario
    b=int(input("Ingresa b: "))
    while True:
        if TM.switches[0]:#opcion suma a+b
            TM.leds[0]=True
            sleep(0.25)
            TM.leds[0]=False
            num_left = a+b
            TM.clearDisplay()
            TM.segments[0]=str(num_left)
            break
        if TM.switches[1]:#resta a-b
            TM.leds[1]=True
            sleep(0.25)
            TM.leds[1]=False
            num_left = a-b
            TM.clearDisplay()
            TM.segments[0]=str(num_left)
            break
        if TM.switches[2]:#multipliacion a*b
            TM.leds[2]=True
            sleep(0.25)
            TM.leds[2]=False
            num_left = a*b
            TM.clearDisplay()
            TM.segments[0]=str(num_left)
            break
        if TM.switches[3]:#division a/b
            TM.leds[3]=True
            sleep(0.25)
            TM.leds[3]=False
            num_left = a/b
            TM.clearDisplay()
            TM.segments[0]=str(round(num_left,2))
            break
        if TM.switches[4]:#raiz al primer numero
            TM.leds[4]=True
            sleep(0.25)
            TM.leds[4]=False
            num_left = math.sqrt(a)
            TM.clearDisplay()
            TM.segments[0]=str(round(num_left,2))
            break
        if TM.switches[5]:#potencia a^b
            TM.leds[5]=True
            sleep(0.25)
            TM.leds[5]=False
            num_left = a**b
            TM.clearDisplay()
            TM.segments[0]=str(num_left)
            break
        if TM.switches[6]:#limpiar display
            TM.leds[6]=True
            sleep(0.25)
            TM.leds[6]=False
            TM.clearDisplay()
            break
        if TM.switches[7]:#salida
            TM.leds[7]=True
            sleep(0.25)
            TM.leds[7]=False
            TM.clearDisplay()
            sys.exit()
    sleep(3)
