drone = int(input (" qual é o codigo do drone?"))
auto = input(" voce possui autorizacao? (s/n)")

if drone == 999 and auto == "s":
    print (" autorizacao concedida")
else:
    print ("ERRO 01: Drone não identificado. Retornando à base.")

bateria= int(input("qual o nivel da bateria de (0 a 100)?: "))
clima = input("o clima esta (ensolarado/chuvoso): ")
velocidade = float(input("a velocidade do vento em (km/h): "))

if bateria < 10:
    print ("o pouso deve ser AUTORIZADO IMEDIATAMENTE por segurança")

else:
    if (clima == "ensolarado" and velocidade <= 30) or (clima == "chuvoso" and velocidade <= 10):
        print("pouso autorizado")
    else:
        print ("pouso negado, por motivos de clima")

