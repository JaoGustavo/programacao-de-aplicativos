temperatura = float(input("digite o valor da temperatura"))

if temperatura >= 80:
    print("PERIGO! Desligando servidor por superaquecimento!")
elif temperatura >= 50: 
    print("Alerta: Ventoinhas ligadada no maximo!")
elif temperatura <= 50:
    print("Temperatura estavel. Sistema operando noramalmente")