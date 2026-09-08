import banco
import sqlite3

def cadastrar():
    try:
        nome = input("Nome da marca: ").strip()
        pais = input("Pais de origem: ").strip()
        
        assert nome != "", "O nome da marca nao pode ser vazio."
        assert pais != "", "O pais nao pode ser vazio."
        
        conexao, cursor = banco.conectar()
        cursor.execute("INSERT INTO marcas (nome, pais) VALUES (?, ?)", (nome, pais))
        conexao.commit()
        conexao.close()
        print("Marca cadastrada com sucesso!")
        
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")

def listar():
    try:
        conexao, cursor = banco.conectar()
        cursor.execute("SELECT * FROM marcas")
        marcas = cursor.fetchall()
        conexao.close()
        
        if len(marcas) == 0:
            print("Nenhuma marca cadastrada.")
        else:
            for marca in marcas:
                print(f"ID: {marca[0]} | Nome: {marca[1]} | Pais: {marca[2]}")
    except sqlite3.Error as e:
        print(f"Erro ao listar: {e}")

def alterar():
    try:
        id_busca = int(input("ID da marca para alterar: "))
        nome = input("Novo nome da marca: ").strip()
        pais = input("Novo pais da marca: ").strip()
        
        assert nome != "", "O nome nao pode ser vazio."
        assert pais != "", "O pais nao pode ser vazio."
        
        conexao, cursor = banco.conectar()
        cursor.execute("UPDATE marcas SET nome = ?, pais = ? WHERE id = ?", (nome, pais, id_busca))
        conexao.commit()
        conexao.close()
        print("Marca alterada com sucesso!")
    except ValueError:
        print("O ID precisa ser um numero.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")

def excluir():
    try:
        id_busca = int(input("ID da marca para excluir: "))
        conexao, cursor = banco.conectar()
        cursor.execute("DELETE FROM marcas WHERE id = ?", (id_busca,))
        conexao.commit()
        conexao.close()
        print("Marca excluida!")
    except ValueError:
        print("O ID precisa ser um numero.")
    except sqlite3.Error:
        print("Nao foi possivel excluir.")
