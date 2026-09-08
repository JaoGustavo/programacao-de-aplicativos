lista_alunos = []

def criar():
    id_aluno = int(input("Digite o ID: "))
    nome = input("Digite o nome do aluno: ")
    aluno = {"id": id_aluno, "nome": nome}
    lista_alunos.append(aluno)
    print("Aluno adicionado!")

def listar():
    if len(lista_alunos) == 0:
        print("Nenhum aluno encontrado.")
    else:
        for aluno in lista_alunos:
            print(f"ID: {aluno['id']} - Nome: {aluno['nome']}")

def atualizar():
    id_busca = int(input("Digite o ID do aluno que quer alterar: "))
    for aluno in lista_alunos:
        if aluno['id'] == id_busca:
            aluno['nome'] = input("Digite o novo nome: ")
            print("Aluno alterado!")
            return
    print("Aluno nao encontrado.")

def excluir():
    id_busca = int(input("Digite o ID do aluno que quer excluir: "))
    for aluno in lista_alunos:
        if aluno['id'] == id_busca:
            lista_alunos.remove(aluno)
            print("Aluno excluido!")
            return
    print("Aluno nao encontrado.")

def menu_alunos():
    opcao = 0
    while opcao != 5:
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Voltar")
        opcao = int(input("Opcao: "))
        
        if opcao == 1:
            criar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            excluir()
