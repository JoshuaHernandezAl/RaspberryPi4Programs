#modulo de limpieza para informacion "colgada" por crasheo o interrupcion
import TM1638



DIO = 17
CLK = 27
STB = 22


display = TM1638.TM1638(DIO, CLK, STB)

display.enable(1)
k=0
while k<=7:
        display.send_char(k,0b00000000)
        k+=1
