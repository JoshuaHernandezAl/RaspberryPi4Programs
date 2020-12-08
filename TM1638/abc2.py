#importar los modulos/bibliotecas de python a utilizar
import TM1638
import time


#defirnir los pin a usar en protocolo BCM
DIO = 17
CLK = 27
STB = 22

#intanciar el objeto 
display = TM1638.TM1638(DIO, CLK, STB)

#habilitar el display
display.enable(1)

#crear lista que servira como base de datos para el programa
#todo en binario ya que el metodo send chat recibe numeros binarios
seg7=[0b1110111,0b1111100,0b111001,0b1011110,0b1111001,0b1110001,0b1101111,0b1110110,0b110000,0b1110,0b1010110,0b111000,0b110111,0b1010100,0b111111,0b1110011,
      0b10111111, 0b11110111, 0b1101101,0b11100, 0b111110,0b10111110,0b11110110,0b1100110,0b11011011,0b110,0b1011011,0b1001111,0b1100110,0b1101101,0b1111101,
      0b111,0b1111111,0b1100111,0b111111]
#importante: la manera en que se condifico la lista seg7 esta hecha para un interpretacion propia de como cree cada letra/numero con los 7 segmentos

#variables de control
i=0
j=0
k=0
a=0
s=0
d=0
f=0
g=0
h=0
z=0
    
#ciclo de recorrida de lista
while i<35:
    a=i+1#posiciones para los display en relacion a la lista
    s=i+2
    d=i+3
    f=i+4
    g=i+5
    h=i+6
    z=i+7
    #despligue en display
    if i<35:#condicion de uso del display
        display.send_char(0,seg7[i])
    else: #apagar en caso contrario
        display.send_char(0,0b00000000)
    if a<35:
        display.send_char(1,seg7[a])
    else: 
        display.send_char(1,0b00000000)
    if s<35:
        display.send_char(2,seg7[s])
    else: 
        display.send_char(2,0b00000000)
    if d<35:
        display.send_char(3,seg7[d])
    else: 
        display.send_char(3,0b00000000)
    if f<35:
        display.send_char(4,seg7[f])
    else: 
        display.send_char(4,0b00000000)
    if g<35:
        display.send_char(5,seg7[g])
    else: 
        display.send_char(5,0b00000000)
    if h<35:
        display.send_char(6,seg7[h])
    else: 
        display.send_char(6,0b00000000)
    if z<35:
        display.send_char(7,seg7[z])
    else: 
        display.send_char(7,0b00000000)
    time.sleep(1)#visualizacion
    i=z+1
time.sleep(5)
k=0
#limpieza de display
while k<=7:
        display.send_char(k,0b00000000)
        k+=1
