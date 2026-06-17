id = (input("Digite seu ID de usuario: "))
valor = int(input("Digite o valor da compra: "))

if id  % 2  == 0 and valor > 500:
    print ("Parabéns, usuário {id}! Você ganhou um cupom para sua compra de R$ {valor}")
else:
    print ("Obrigado pela compra, usuário {id}. Continue acompanhando nossas promoções!")
