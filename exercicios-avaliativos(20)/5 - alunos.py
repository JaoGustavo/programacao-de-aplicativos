import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")

    try:
        id_turma = int(input("Digite o ID numerico da turma:"))
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id turma) VALUES (?, ?)", ('nome', 'id_turma'))
        conexao.commit()
    except ValueError:
        print("Erro: Digite apenas numeros!")
    except sqlite3.Error:
        print("Erro no banco de dados!")
    finally:
        conexao.close()


        import sqlite3

#  A conversão int() gera um ValueError se o usuario digitar texto.



