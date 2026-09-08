import banco
import sqlite3

def cadastrar():
    try:
        nome_modelo = input("Nome do modelo: ").strip()
        id_marca = int(input("ID da Marca: "))
        
        assert nome_modelo != "", "O nome do modelo nao pode ser vazio."
        assert id_marca > 0, "ID da marca deve ser maior que zero."
        
        conexao, cursor = banco.conectar()
        cursor.execute("INSERT INTO modelos (nome_modelo, id_marca) VALUES (?, ?)", (nome_modelo, id_marca))
        conexao.commit()
        conexao.close()
        print("Modelo cadastrado com sucesso!")
        
    except ValueError:
        print("Digite apenas numeros para o ID da marca.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error:
        print("Essa marca nao existe no banco de dados.")

def listar():
    try:
        conexao, cursor = banco.conectar()
        cursor.execute("SELECT * FROM modelos")
        modelos = cursor.fetchall()
        conexao.close()
        
        if len(modelos) == 0:
            print("Nenhum modelo cadastrado.")
        else:
            for modelo in modelos:
                print(f"ID: {modelo[0]} | Modelo: {modelo[1]} | ID Marca: {modelo[2]}")
    except sqlite3.Error as e:
        print(f"Erro ao listar: {e}")

def alterar():
    try:
        id_busca = int(input("ID do modelo para alterar: "))
        nome_modelo = input("Novo nome do modelo: ").strip()
        id_marca = int(input("Novo ID da marca: "))
        
        assert nome_modelo != "", "O nome do modelo nao pode ser vazio."
        assert id_marca > 0, "ID da marca deve ser maior que zero."
        
        conexao, cursor = banco.conectar()
        cursor.execute("UPDATE modelos SET nome_modelo = ?, id_marca = ? WHERE id = ?", (nome_modelo, id_marca, id_busca))
        conexao.commit()
        conexao.close()
        print("Modelo alterado!")
    except ValueError:
        print("Digite numeros validos.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error:
        print("Nao foi possivel alterar.")

def excluir():
    try:
        id_busca = int(input("ID do modelo para excluir: "))
        conexao, cursor = banco.conectar()
        cursor.execute("DELETE FROM modelos WHERE id = ?", (id_busca,))
        conexao.commit()
        conexao.close()
        print("Modelo excluido!")
    except ValueError:
        print("O ID precisa ser um numero.")
    except sqlite3.Error:
        print("Nao foi possivel excluir.")
