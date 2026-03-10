garrafas = int(input("digite o numero de garrafas: "))

if garrafas % 500 == 0:
    print ("HORA DA LIMPEZA: Parar máquina imediatamente! ")

if garrafas % 100 == 0:
    print ("QUALIDADE, retire uma garrafa para conferir")

