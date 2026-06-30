import sqlite3 
def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    #se o id_prof nao existir, ocorre um IbtergityError.
    #como restringir isso direto na estrutura da tabela abaixo?
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTERGER PRIMARY LEY AUTOINCREMENT,
                   nome TEXT,
                   cpf TEXT
            )
        ''')
    
