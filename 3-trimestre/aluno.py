def listar_alunos(conexao):
    cursor = conexao.cursor()
    sql = "SELECT id, nome, matricula FROM aluno ORDER BY nome ASC;"
    
    cursor.execute(sql)
    alunos = cursor.fetchall()
    return alunos