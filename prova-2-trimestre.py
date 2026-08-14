
import sqlite3

try:
    conexao = sqlite3.connect('transportadora.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transportadoras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_fantasia TEXT NOT NULL,
            cnpj TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS garagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade TEXT NOT NULL,
            id_transportadora INTEGER NOT NULL,
            FOREIGN KEY (id_transportadora) REFERENCES transportadoras (id)
        )
    ''')
    conexao.commit()
except sqlite3.Error:
        print("Erro ao inicializar o banco de dados.")
finally:
    conexao.close()


def cadastrar_transportadora():
    try:
        nome_fantasia = input("Nome: ")
        cnpj = int(input("CNPJ: "))

        conexao = sqlite3.connect('transportadora.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO transportadoras (nome_fantasia, cnpj) VALUES (?, ?)", (nome_fantasia, cnpj))
        conexao.commit()
        print("Transportadora cadastrad!")
    except sqlite3.IntegrityError:
        print("Este CNPJ ja esta cadastrado.")
    except sqlite3.Error:
        print("Erro no banco de dados ao cadastrar transportadora.")
    finally:
        conexao.close()


def cadastrar_garagem():
    try:        
        id_transportadora = int(input("Digite o ID da Transportadora: "))
        cidade = input("Cidade da Garagem: ")

        conexao = sqlite3.connect('transportadora.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT id FROM transportadoras WHERE id = ?", (id_transportadora,))

        if cursor.fetchone() is None:
            print("ID de transportadora nao encontrada.")
            conexao.close()
            return

        cursor.execute("INSERT INTO garagens (cidade, id_transportadora) VALUES (?, ?)", (cidade, id_transportadora))
        conexao.commit()
        print("Garagem cadastrada!")
    except ValueError:
        print("Entrada invalida. O ID deve ser um numero inteiro.")
    except sqlite3.Error:
        print("Erro no banco de dados ao cadastrar garagem.")
    finally:
        conexao.close()


def listar_transportadoras():
    try:        
        print("Listando tranportadoras")
        print("    ")

        conexao = sqlite3.connect('transportadora.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome_fantasia, cnpj FROM transportadoras")
        linhas = cursor.fetchall()

        if not linhas:
            print("Nenhuma transportadora encontrada.")
        else:
            for linha in linhas:
                print(f"ID: {linha[0]} | Nome: {linha[1]} | CNPJ: {linha[2]}")
    except sqlite3.Error:
        print("Erro ao listar transportadoras.")
    finally:
        conexao.close()


def listar_garagens():
    try:        
        print("Listadno garagens")
        print("    ")

        conexao = sqlite3.connect('transportadora.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id, cidade, id_transportadora FROM garagens")
        linhas = cursor.fetchall()

        if not linhas:
            print("Nenhuma garagem encontrada.")
        else:
            for linha in linhas:
                print(f"ID Garagem: {linha[0]} | Cidade: {linha[1]} | ID Transportadora: {linha[2]}")
    except sqlite3.Error:
        print("Erro ao listar garagens.")
    finally:
        conexao.close()


def atualizar_transportadora():
    try:
        print("Atualizando nome da transportadora.")
        print("    ")

        id_transportadora = int(input("Digite o ID da transportadora que voce ira atualizar: "))
        novo_nome_fantasia = input("Novo Nome: ")
        novo_cnpj = int(input("Novo CNPJ: "))

        if not novo_nome_fantasia or not novo_cnpj:
            print("Nenhum campo pode ser vazio")
            return

        conexao = sqlite3.connect('transportadora.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM transportadoras WHERE id = ?",(id_transportadora,))

        if cursor.fetchone() is None:
            print("Transportadora nao existe.")
            conexao.close()
            return

        cursor.execute("UPDATE transportadoras SET nome_fantasia = ?, cnpj = ? WHERE id = ?", (novo_nome_fantasia, novo_cnpj, id_transportadora))
        conexao.commit()
        print("Transportadora atualizada!")

    except ValueError:
        print(" O ID deve ser um numero inteiro.")
    except sqlite3.IntegrityError:
        print("Este CNPJ ja esta em uso por outra transportadora.")
    except sqlite3.Error:
        print("Erro no banco de dados.")
    finally:
        conexao.close()


def atualizar_garagem():
    try:        
        print("Atualizando nome da garagem.")
        print("    ")

        id_garagem = int(input("Digite o ID da garagem que voce ira atualizar: "))
        nova_cidade = input("Nova Cidade: ")
        novo_id_transportadora = int(input("Novo ID da Transportadora vinculada: "))
        conexao = sqlite3.connect('transportadora.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT id FROM garagens WHERE id = ?", (id_garagem,))
        if cursor.fetchone() is None:
            print("Garagem nao encontrada.")
            conexao.close()
            return

        cursor.execute("SELECT id FROM transportadoras WHERE id = ?", (novo_id_transportadora,))
        if cursor.fetchone() is None:
            print("Transportadora nao encontrada.")
            conexao.close()
            return

        cursor.execute("UPDATE garagens SET cidade = ?, id_transportadora = ? WHERE id = ?", (nova_cidade, novo_id_transportadora, id_garagem))
        conexao.commit()
        print("Garagem atualizada!")
    except ValueError:
        print("Digite o numero do ID corretamente")
    except sqlite3.Error:
        print("Erro no banco de dados.")
    finally:
        conexao.close()


def excluir_transportadora():
    try:        
        print("Excluindo transportadora.")
        print("    ")
        
        id_transportadora = int(input("Digite o ID da transportadora que voce vai excluir: "))
        conexao = sqlite3.connect('transportadora.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM transportadoras WHERE id = ?", (id_transportadora,))
        if cursor.fetchone() is None:
            print("Transportadora nao encontrada.")
            conexao.close()
            return
        cursor.execute("DELETE FROM garagens WHERE id_transportadora = ?", (id_transportadora,))
        cursor.execute("DELETE FROM transportadoras WHERE id = ?", (id_transportadora,))
        conexao.commit()
        print("Transportadora excluida.")
    except ValueError:
        print("O ID deve ser um numero inteiro.")
    except sqlite3.Error:
        print("Erro ao excluir transportadora.")
    finally:
        conexao.close()


def excluir_garagem():
    try:        
        print("Excluindo garagem") 
        print("    ")

        id_garagem = int(input("Digite o ID da garagem que deseja excluir: "))
        conexao = sqlite3.connect('transportadora.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM garagens WHERE id = ?", (id_garagem,))
        if cursor.fetchone() is None:
            print("Garagem nao encontrada.")
            conexao.close()
            return
        cursor.execute("DELETE FROM garagens WHERE id = ?", (id_garagem,))
        conexao.commit()
        print("Garagem excluida!")
    except ValueError:
        print("O ID deve ser um numero inteiro.")
    except sqlite3.Error:
        print("Erro ao excluir a garagem.")
    finally:
        conexao.close()


def menu():

    while True:
        try:
            print("\n-- Sistema de Frota de Transportes --")
            print("1. Cadastrar Transportadora")
            print("2. Cadastrar Garagem")
            print("3. Listar Transportadoras")
            print("4. Listar Garagens")
            print("5. Atualizar Transportadora")
            print("6. Atualizar Garagem")
            print("7. Excluir Transportadora")
            print("8. Excluir Garagem")
            print("9. Sair")
            
            opcao = input("Escolha uma opcao: ")
            
            if opcao == "1":
                cadastrar_transportadora()
            elif opcao == "2":
                cadastrar_garagem()
            elif opcao == "3":
                listar_transportadoras()
            elif opcao == "4":
                listar_garagens()
            elif opcao == "5":
                atualizar_transportadora()
            elif opcao == "6":
                atualizar_garagem()
            elif opcao == "7":
                excluir_transportadora()
            elif opcao == "8":
                excluir_garagem()
            elif opcao == "9":
                print("Saindo")
                break
            else:
                print("Opcao nao existe.")
        except Exception:
            print("Ocorreu um erro no menu.")

menu()