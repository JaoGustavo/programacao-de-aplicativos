import sqlite3
conexao = sqlite3.connect('escola.demosntracao.db')
cursor = conexao.cursor()


def cadastrar_professor():
    nome_completo = input("Digite o nome completo: ")
    telefone_professor = input("Digite o telefone: ")
    materia = input("Digite a Turma: ")
    idade_professor = int(input("Digite a idade: "))
    cpf = input("Digite o cpf: ")
    salario = float(input("Digite seu salario: "))
    escola = (input("Digite o nome da escola: "))

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT, 
                turma TEXT, 
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL
                salario TEXT,
                escola TEXT NOT NULL)''')
    comando_inserir = f'''
        INSERT INTO alunos(nome, telefone, turma, idade, cpf)
        VALUES('{nome_completo}', '{telefone_professor}', '{materia}', '{idade_professor}', '{cpf}', {salario}', {escola}' )'''

    cursor.execute(comando_inserir)
    conexao.commit()


def listar():
    conexao.commit()
    cursor.execute("SELECT * FROM alunos")
    for linha in cursor.fetchall():
        print(linha)
    print("\n")



# def alterar():



def excluir():
    id_professor = input("Digite o ID do professor que deseja excluir: ")
    cursor.execute(
        "DELETE FROM alunos WHERE id = ?", (id_professor,)
    )

    conexao.commit()
    if cursor.rowcount > 0 :
        print("Professor excluido com sucesso.")
    else:
        print("Nenhum professor encontrado com esse ID. ")


def Menu():
    inicializar_banco()
    
while True:
    print("1 - CADASTRAR ALUNO\n2 - LISTAR ALUNOS\n3 - BUSCAR ALUNO\n4 - ATUALIZAR DADOS\n5 - EXCLUIR CADASTRO\n6 - FECHAR PROGRAMA ")
    opcao_while = int(input("Qual ação deseja realizar: "))
        
        if opcao == "1":
            criar_professor()
        elif opcao == "2":
            listar_professores()
        elif opcao == "3":
            alterar_professor()
        elif opcao == "4":
            excluir_professor()
        elif opcao == "5":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Escolha um número entre 1 e 5.")
