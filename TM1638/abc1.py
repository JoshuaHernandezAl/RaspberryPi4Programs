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
#seg7 tiene la sig estructura A-Z 0-9

#variables de control
i=0
j=0
k=0
    
    
#cilco de recorrida de la lista
for i in seg7:
    if j<=7: #condicion de despliegue a displays
        display.send_char(j,i)#metodo de impresion recibe posicion y dato binario (j,i)
        time.sleep(0.5)#suspension de programa para visualizacion
        j+=1#variable de control para despligue en display
    else:
        while k<=7:#ciclo de limpieza de display
            display.send_char(k,0b00000000)
            k+=1
        j=0#reset de variables de control para un nuevo despliegue sin exceder el rango de modulo tm1638
        k=0
        display.send_char(j,i)
        time.sleep(0.5)
        j+=1
time.sleep(3)#sleep para visualizacion
k=0
#ciclo de limpieza, impide que se quede informacion desplegada en los display
while k<=7:
      display.send_char(k,0b00000000)
      k+=1
