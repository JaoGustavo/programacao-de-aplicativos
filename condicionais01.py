nome = input("digite seu nome")
altura = float(input("digite sua altura"))

if altura >= 1.50:
    print ("Acesso liberado! Divirta-se na queda livre", nome)
elif altura < 1.50:
    print ("desculpe, você não tem altura minima", nome)