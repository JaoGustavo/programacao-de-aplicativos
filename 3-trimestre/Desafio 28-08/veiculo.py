import banco
import sqlite3

def cadastrar():
    try:
        placa = input("Placa do veiculo: ").strip()
        ano = int(input("Ano do veiculo: "))
        id_modelo = int(input("ID do Modelo: "))
        
        assert placa != "", "A placa do veiculo nao pode ser vazia."
        assert ano >= 1900, "O ano do veiculo deve ser igual ou superior a 1900."
        
        conexao, cursor = banco.conectar()
        cursor.execute("INSERT INTO veiculos (placa, ano, id_modelo) VALUES (?, ?, ?)", (placa, ano, id_modelo))
        conexao.commit()
        conexao.close()
        print("Veiculo cadastrado com sucesso!")
        
    except ValueError:
        print("Ano e ID do modelo precisam ser numeros.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error:
        print("Esse modelo nao existe no banco de dados.")

def listar():
    try:
        conexao, cursor = banco.conectar()
        cursor.execute("SELECT * FROM veiculos")
        veiculos = cursor.fetchall()
        conexao.close()
        
        if len(veiculos) == 0:
            print("Nenhum veiculo cadastrado.")
        else:
            for veiculo in veiculos:
                print(f"ID: {veiculo[0]} | Placa: {veiculo[1]} | Ano: {veiculo[2]} | ID Modelo: {veiculo[3]}")
    except sqlite3.Error as e:
        print(f"Erro ao listar: {e}")

def alterar():
    try:
        id_busca = int(input("ID do veiculo para alterar: "))
        placa = input("Nova placa do veiculo: ").strip()
        ano = int(input("Novo ano do veiculo: "))
        id_modelo = int(input("Novo ID do modelo: "))
        
        assert placa != "", "A placa nao pode ser vazia."
        assert ano >= 1900, "O ano deve ser igual ou maior que 1900."
        
        conexao, cursor = banco.conectar()
        cursor.execute("UPDATE veiculos SET placa = ?, ano = ?, id_modelo = ? WHERE id = ?", (placa, ano, id_modelo, id_busca))
        conexao.commit()
        conexao.close()
        print("Veiculo alterado!")
    except ValueError:
        print("Digite dados numericos validos.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error:
        print("Nao foi possivel alterar. Verifique se o modelo existe.")

def excluir():
    try:
        id_busca = int(input("ID do veiculo para excluir: "))
        conexao, cursor = banco.conectar()
        cursor.execute("DELETE FROM veiculos WHERE id = ?", (id_busca,))
        conexao.commit()
        conexao.close()
        print("Veiculo excluido!")
    except ValueError:
        print("O ID precisa ser um numero.")
