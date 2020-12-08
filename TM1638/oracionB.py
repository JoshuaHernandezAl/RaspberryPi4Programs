##importar los modulos/bibliotecas de python a utilizar
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
      0b111,0b1111111,0b1100111,0b111111, 0b01000110,0b01010011, 0b00000000, 0b10000000, 0b00000100]
#importante: la manera en que se condifico la lista seg7 esta hecha para un interpretacion propia de como cree cada letra/numero con los 7 segmentos
msg=input("Ingresa texto: ")#solicitud al usuario
msg7=[]
for i in msg:#albergar informacion para despliegue en 7 segmentos
    if i=='a' or i=='A':
        msg7.append(seg7[0])
    elif i=='b' or i=='B':
        msg7.append(seg7[1])
    elif i=='c' or i=='C':
        msg7.append(seg7[2])
    elif i=='d' or i=='D':
        msg7.append(seg7[3])
    elif i=='e' or i=='E':
        msg7.append(seg7[4])
    elif i=='f' or i=='F':
        msg7.append(seg7[5])
    elif i=='g' or i=='G':
        msg7.append(seg7[6])
    elif i=='h' or i=='H':
        msg7.append(seg7[7])
    elif i=='i' or i=='I':
        msg7.append(seg7[8])
    elif i=='j' or i=='J':
        msg7.append(seg7[9])
    elif i=='k' or i=='K':
        msg7.append(seg7[10])
    elif i=='l' or i=='L':
        msg7.append(seg7[11])
    elif i=='m' or i=='M':
        msg7.append(seg7[12])
    elif i=='n' or i=='N':
        msg7.append(seg7[13])
    elif i=='o' or i=='O':
        msg7.append(seg7[14])
    elif i=='p' or i=='P':
        msg7.append(seg7[15])
    elif i=='q' or i=='Q':
        msg7.append(seg7[16])
    elif i=='r' or i=='R':
        msg7.append(seg7[17])
    elif i=='s' or i=='S':
        msg7.append(seg7[18])
    elif i=='u' or i=='U':
        msg7.append(seg7[19])
    elif i=='v' or i=='V':
        msg7.append(seg7[20])
    elif i=='w' or i=='W':
        msg7.append(seg7[21])
    elif i=='x' or i=='X':
        msg7.append(seg7[22])
    elif i=='y' or i=='Y':
        msg7.append(seg7[23])
    elif i=='z' or i=='Z':
        msg7.append(seg7[24])
    elif i=='1':
        msg7.append(seg7[25])
    elif i=='2':
        msg7.append(seg7[26])
    elif i=='3':
        msg7.append(seg7[27])
    elif i=='4':
        msg7.append(seg7[28])
    elif i=='5':
        msg7.append(seg7[29])
    elif i=='6':
        msg7.append(seg7[30])
    elif i=='7':
        msg7.append(seg7[31])
    elif i=='8':
        msg7.append(seg7[32])
    elif i=='9':
        msg7.append(seg7[33])
    elif i=='0':
        msg7.append(seg7[34])
    elif i=='t' or i=='T':
        msg7.append(seg7[35])
    elif i=='?':
        msg7.append(seg7[36])
    elif i==' ':
        msg7.append(seg7[37])
    elif i=='.':
        msg7.append(seg7[38])
    elif i==',':
        msg7.append(seg7[39])

i=0
j=0
k=len(msg7)
a=0
s=0
d=0
f=0
g=0
h=0
z=0

#despligue en 7 segmentos a modo de  marquesina
while k != 0:#rige el ciclo respecto a la longitud de la lista
    msg7b=msg7
    while i < len(msg7b):
        if i<=7:
            display.send_char(i,msg7b[i])#despliga la informacion en los display 
        i +=1
    msg7.pop(0)#utilizamos pop para remover la posicion 0 en de la lista correpondiete al primer caracter del mensaje
    k=len(msg7) #reset a K en longitud del mensaje (recordar que se disminuyo en uno de manera dinamica)
    i=0#reset a i para volver a ingresar al cilo de despligue
    time.sleep(0.5)#visualizacion
    l=0#limpieza de los display previene la sobre escritura de informacion
    while l<=7:
        display.send_char(l,0b00000000)
        l+=1




