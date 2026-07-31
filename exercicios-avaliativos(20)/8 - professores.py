import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores (
                 id  INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT,
                 cpf UNIQUE TEXT
                 )
                 ''')
    
# O erro era por que o cpf nao estava "UNIQUE" e ele so pode ser unico.