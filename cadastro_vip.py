lista_vip = []
nome = ("Digite o nome do convidado (ou 'fim' se finalizado): ")

while nome != "fim":
    nome = input("Digite o nome do convidado (ou 'fim' para encerrar): ")
    
    if nome != "fim":
        if nome[0] == "A":
            lista_vip.append(nome)
        else:
            print("Apenas nomes com A são permitidos no VIP")

print ("lista VIP:", lista_vip)
    
