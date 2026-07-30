import sqlite3 
 
def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    tabelas_permitidas = ["alunos", "professores", "series", "turmas"]

    if nome_tabela not in tabelas_permitidas:
        print("Tabela inválida!")
        return

    sql = f"SELECT * FROM {nome_tabela} WHERE id = ?"
    cursor.execute(sql, (id_registro,))

    print(cursor.fetchone())
    
    conexao.close()

# Não pode se usar colunas ou tabelas como parâmetros."