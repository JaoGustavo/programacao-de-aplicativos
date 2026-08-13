
import sqlite3

try:
    conexao = sqlite3.connect('hospital.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hospitais(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cidade TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        crm TEXT UNIQUE NOT NULL,
        id_hospital INTEGER NOT NULL,
        FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
    )
    ''')
    conexao.commit()

except sqlite3.Error as erro:
    print(f"Erro ao conectar ou criar o banco de dados: {erro}")
    exit()


def cadastrar_hospital():
    try:
        nome = input("Digite o nome do hospital: ")
        cidade = input("Digite a cidade do hospital: ")

        comando_inserir = f'''
        INSERT INTO hospitais(nome, city) 
        VALUES('{nome}', '{cidade}')'''
        
        comando_inserir = f'''
        INSERT INTO hospitais(nome, cidade) 
        VALUES('{nome}', '{cidade}')'''

        cursor.execute(comando_inserir)
        conexao.commit()
        print("Hospital cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados ao cadastrar hospital: {erro}")


def cadastrar_medico():
    try:
        nome_medico = input("Digite o nome do médico: ")
        crm = input("Digite o CRM: ")
        id_hospital = int(input("Digite o ID do Hospital de vínculo: "))

        comando_inserir = f'''
        INSERT INTO medicos(nome, crm, id_hospital)
        VALUES('{nome_medico}', '{crm}', {id_hospital})'''

        cursor.execute(comando_inserir)
        conexao.commit()
        print("Médico cadastrado com sucesso!")

    except ValueError:
        print("Erro: O ID do hospital deve ser um número inteiro válido.")
    except sqlite3.IntegrityError as erro:

        mensagem_erro = str(erro)
        if "FOREIGN KEY constraint failed" in mensagem_erro:
            print("Erro: O ID do hospital informado NÃO existe no sistema.")
        else:
            print("Erro: Já existe um médico cadastrado com este CRM.")
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados ao cadastrar: {erro}")


def listar_hospitais():
    try:
        cursor.execute("SELECT * FROM hospitais")
        linhas = cursor.fetchall()
        
        if not linhas:
            print("Nenhum hospital cadastrado.")
        else:
            print("\n--- LISTA DE HOSPITAIS ---")
            for linha in linhas:
                print(f"ID: {linha[0]} | Nome: {linha[1]} | Cidade: {linha[2]}")
        print("\n")
    except sqlite3.Error as erro:
        print(f"Erro ao listar hospitais: {erro}")


def listar_medicos():
    try:
        cursor.execute("SELECT * FROM medicos")
        linhas = cursor.fetchall()
        
        if not linhas:
            print("Nenhum médico cadastrado.")
        else:
            print("\n--- LISTA DE MÉDICOS ---")
            for linha in linhas:
                print(f"ID: {linha[0]} | Nome: {linha[1]} | CRM: {linha[2]} | ID Hospital: {linha[3]}")
        print("\n")
    except sqlite3.Error as erro:
        print(f"Erro ao listar médicos: {erro}")

def menu():
    while True:
        try:
            print("\n1. Cadastrar Hospital")
            print("2. Cadastrar Médico")
            print("3. Listar Hospitais")
            print("4. Listar Médicos")
            print("5. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                cadastrar_hospital()
            elif opcao == '2':
                cadastrar_medico()
            elif opcao == '3':
                listar_hospitais()
            elif opcao == '4':
                listar_medicos()
            elif opcao == '5':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")
                
        except KeyboardInterrupt:
            print("\n\nExecução interrompida. Fechando o sistema de forma segura...")
            break
        except Exception as erro:
            print(f"Ocorreu um erro inesperado no menu: {erro}")
            
    try:
        conexao.close()
    except:
        pass

menu()


