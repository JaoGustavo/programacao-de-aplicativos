lista_cursos = []

def criar():
    id_curso = int(input("Digite o ID: "))
    nome = input("Digite o nome do curso: ")
    curso = {"id": id_curso, "nome": nome}
    lista_cursos.append(curso)
    print("Curso adicionado!")

def listar():
    if len(lista_cursos) == 0:
        print("Nenhum curso encontrado.")
    else:
        for curso in lista_cursos:
            print(f"ID: {curso['id']} - Nome: {curso['nome']}")

def atualizar():
    id_busca = int(input("Digite o ID do curso que quer alterar: "))
    for curso in lista_cursos:
        if curso['id'] == id_busca:
            curso['nome'] = input("Digite o novo nome: ")
            print("Curso alteredo!")
            return
    print("Curso nao encontrado.")

def excluir():
    id_busca = int(input("Digite o ID do curso que quer excluir: "))
    for curso in lista_cursos:
        if curso['id'] == id_busca:
            lista_cursos.remove(curso)
            print("Curso excluido!")
            return
    print("Curso nao encontrado.")

def menu_cursos():
    opcao = 0
    while opcao != 5:
        print("\n--- MENU CURSOS ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar")
        opcao = int(input("Opcao: "))
        
        if opcao == 1:
            criar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            excluir()
