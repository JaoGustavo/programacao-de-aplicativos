import sqlite3

# O relatorio roda, mas repete os dados erroneamente em formato de matriz cruzada
# porque falta definir a regra de colagem (vinculo). Conserte o comando SQL:
def listar_alunos_e_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas")

    for linha in cursor.fechall():
        print(f"Aluno: {linha[0]} | Turma:{linhas[1]}")
    conexao.close