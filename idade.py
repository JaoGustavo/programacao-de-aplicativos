idade = int (input("digite sua idade"))
saldo = float(input("digite seu saldo"))

if idade >= 18 and saldo >= 50.0:
    print ("Acesso autorizado, Bem vindo ao evento")
else:
    print ("Infelizmente voce nao cumpriu os requisistos de entrada")