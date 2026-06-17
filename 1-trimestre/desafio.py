nome = str(input("digite seu nome"))
valor_total = float(input("digite o vslor total da compra"))
distancia_da_entrega = int(input("digite a distancia da entrega"))
cupom = input ("possui cupom especial? (S/N)")

desconto_percentual = 0.0
ganhou_brinde = True


if valor_total >= 1.000 and cupom == "S":
    desconto_percentual = 0.20 
    ganhou_brinde = True
elif 500 < valor_total < 1.000 and cupom == "S":
    desconto_percentual = 0.10

valor_desconto = valor_total * desconto_percentual
valor_desconto = valor_total - valor_desconto

if distancia_da_entrega <= 50 and valor_desconto > 200:
   frete = 0.00
else:
    frete = 40.00

total_final = valor_desconto +frete

print ("/n" + "="*30)
print ("resumo")
print ("="*30)
print ("client: nome")
print ("valor original:", valor_total)
print ("Desconto aplicado:", valor_desconto)
print ("total final:", total_final)
print ("="*30)

if ganhou_brinde:
    print ("Parabens voce ganhou o mouse pad gamer")


    
