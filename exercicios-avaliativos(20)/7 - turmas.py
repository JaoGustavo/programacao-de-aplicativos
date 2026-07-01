import sqlite3 
def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")



    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTERGER PRIMARY LEY AUTOINCREMENT,
                   nome TEXT,
                   cpf TEXT
            )
        ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS turmas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        id_serie INTEGER,
        id_prof INTEGER,
        FOREIGN KEY (id_prof) REFERENCES professores(id)
    )
    ''')
    
    conexao.commit()
    conexao.close()

# Precisa adicionar uma tabela para os professores