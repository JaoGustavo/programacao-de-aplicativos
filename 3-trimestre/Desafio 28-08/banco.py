import sqlite3

def conectar():
    conexao = sqlite3.connect("gestao_concessionaria.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    return conexao, cursor

def criar_tabelas():
    conexao, cursor = conectar()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS marcas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        pais TEXT NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS modelos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_modelo TEXT NOT NULL,
        id_marca INTEGER NOT NULL,
        FOREIGN KEY (id_marca) REFERENCES marcas(id)
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS veiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        placa TEXT NOT NULL,
        ano INTEGER NOT NULL,
        id_modelo INTEGER NOT NULL,
        FOREIGN KEY (id_modelo) REFERENCES modelos(id)
    );
    """)
    
    conexao.commit()
    conexao.close()

criar_tabelas()
