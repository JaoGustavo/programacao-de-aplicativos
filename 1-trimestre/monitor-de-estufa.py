temperatura = float(input("digite a temperatura atual"))

if temperatura <= 30.0:
    print ("tempertaura estavel")
elif temperatura > 30.0:
    print ("alerta de calor")

umidade = float(input("qual é a umidade"))
if umidade < 40.0:
    print ("alerta ligue a irrigaçao")
elif umidade > 40.0:
    print ("ligue as ventoinhas")