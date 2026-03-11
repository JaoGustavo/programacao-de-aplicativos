codigo = int(input("digite seu codigo: "))
peso = int(input("qual o peso da carga em kg? "))
status = "carga noramal"

if peso < 5 and codigo % 10 == 0:
    status = "carga normal"

if peso > 50:
    status = "carga pesada"

print (f"pacote {codigo}: {status}")

    

