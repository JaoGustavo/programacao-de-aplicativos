idade = int(input("digite sua idade"))
ingresso = input ("voce tem o ingresso? (s/n):")
lista = input("voce esta na lista? (s/n):")

if idade >= 18 and ingresso == "s" or lista =="s":
    print ("acesso liberado")
else:
    print ("acesso nao autorizado")