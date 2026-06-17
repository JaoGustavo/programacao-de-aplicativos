vagas = ["Livre", "Ocupado", "Livre", "Ocupado"]
digite = int(input("digite o numero de 0 a 3: "))

if 0 <= digite < 3:
    if digite % 2 == 0 and vagas[digite] == "Livre":
        print(f"Vaga {digite} autorizada para estacionar.")
    else:
        print(f"Vaga {digite} indisponivel ou fora das regras")
else:
    print ("indice invalido")