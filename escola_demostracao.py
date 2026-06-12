import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

novo_nome = "Joao Sareto"
novo_cpf = "123.456.789.10"
aluno_id = 1 

sql = """
UPDATE Alunos
SET nome = ?, cpf = ?
WHERE id = ?
"""

try: 
    cursor.execute (sql, (novo_nome, novo_cpf, aluno_id))
    conexao.commit()
    print ("Dados do aluno atualizado com sucesso!")

except sqlite3.Error as erro:
    print (f"Erro ao atualizar banco de dados: {erro}")

finally:
    conexao.close()
    