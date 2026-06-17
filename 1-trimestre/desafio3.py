saldo = 1000.00

print ("1 - deposito ")
print ("2 - saque ")
print ("3 - extrato")

opcoes = input("escolha uma opcao ")

if opcoes == "1":
    valor = float (input("digite o valor do seu deposito: "))
    valor_deposito = saldo + valor 
    print ("seu deposito é: ", valor_deposito)

if opcoes == "2":
    saque = float(input("digite o valor que voce quer sacar"))
    valor_saque = saldo - saque
    print ("seu saldo agora é: ", valor_saque)

if opcoes == "3":
    extrato = saldo
    print ("seu saldo atual é:", saldo)
