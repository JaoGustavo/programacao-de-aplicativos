def criar_arquivo():
    open ('viagem.txt','w').close()

def criar():
    nome = input("Adicione o seu destino: ")
    with open('viagem.txt', 'a') as f:
        f.write(nome + '\n')
    print("Local adicionado!")

def ler():
    with open('viagem.txt', 'r') as f:
        viagens = f.readlines()

        i = 0
        for viagem in viagens:
            print(f"{i} - {viagem.strip()}") 
            i += 1 

def atualizar():
    ler() 
    idx = int(input("Digite o ID do local que deseja alterar: "))
    novo_nome = input("Novo local: ")

    with open('viagem.txt', 'r') as f:
        linhas = f.readlines()

    linhas[idx] = novo_nome + '\n'

    with open('viagem.txt', 'w') as f:
        f.writelines(linhas)
    print("Local atualizado!")

def deletar():
    ler()
    idx = int(input("Digite o ID do local que deseja excluir: "))

    with open('viagem.txt', 'r') as f:
        linhas = f.readlines()

    del linhas[idx]

    with open('viagem.txt', 'w') as f:
        f.writelines(linhas)
    print("Local removido!")

while True:
    print("\n1-Adicionar local | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
    opcao = input("Escolha: ")

    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break

