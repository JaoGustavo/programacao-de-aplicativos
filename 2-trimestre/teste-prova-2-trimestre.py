import sqlite3

def inicializar_banco(conexao):
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transportadoras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_fantasia TEXT NOT NULL,
            cnpj TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS garagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade TEXT NOT NULL,
            id_transportadora INTEGER NOT NULL,
            FOREIGN KEY (id_transportadora) REFERENCES transportadoras (id)
        )
    ''')
    conexao.commit()

def db_cadastrar_transportadora(conexao, nome_fantasia, cnpj):
    if not nome_fantasia or not cnpj:
        raise ValueError("Campos vazios")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO transportadoras (nome_fantasia, cnpj) VALUES (?, ?)", (nome_fantasia, cnpj))
    conexao.commit()
    return cursor.lastrowid

def db_cadastrar_garagem(conexao, cidade, id_transportadora):
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM transportadoras WHERE id = ?", (id_transportadora,))
    if cursor.fetchone() is None:
        raise ValueError("ID de transportadora nao encontrada.")
    cursor.execute("INSERT INTO garagens (cidade, id_transportadora) VALUES (?, ?)", (cidade, id_transportadora))
    conexao.commit()
    return cursor.lastrowid

def db_atualizar_transportadora(conexao, id_transportadora, novo_nome, novo_cnpj):
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM transportadoras WHERE id = ?", (id_transportadora,))
    if cursor.fetchone() is None:
        raise ValueError("Transportadora nao existe.")
    cursor.execute("UPDATE transportadoras SET nome_fantasia = ?, cnpj = ? WHERE id = ?", (novo_nome, novo_cnpj, id_transportadora))
    conexao.commit()

def db_excluir_transportadora(conexao, id_transportadora):
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM transportadoras WHERE id = ?", (id_transportadora,))
    if cursor.fetchone() is None:
        raise ValueError("Transportadora nao encontrada.")
    cursor.execute("DELETE FROM garagens WHERE id_transportadora = ?", (id_transportadora,))
    cursor.execute("DELETE FROM transportadoras WHERE id = ?", (id_transportadora,))
    conexao.commit()


def executar_testes_prova():
    print("Iniciando bateria de testes com assert...")

    conexao = sqlite3.connect(':memory:')
    inicializar_banco(conexao)
    cursor = conexao.cursor()

    print("\n[Testando]: Cadastro de Transportadoras")
    
    id_trans1 = db_cadastrar_transportadora(conexao, "Alfa Transportes", "12345678901234")
    assert id_trans1 == 1, "Erro: Primeira transportadora deveria receber ID 1"

    id_trans2 = db_cadastrar_transportadora(conexao, "B", "0")
    assert id_trans2 == 2, "Erro: Falha ao aceitar valores mínimos válidos"

    try:
        db_cadastrar_transportadora(conexao, "Transportadora Clonada", "12345678901234")
        assert False, "Erro: O sistema aceitou um CNPJ duplicado (Falha de Integridade)"
    except sqlite3.IntegrityError:
        pass

    try:
        db_cadastrar_transportadora(conexao, "", "")
        assert False, "Erro: O sistema aceitou strings vazias no cadastro"
    except ValueError:
        pass


    print("[Testando]: Cadastro de Garagens")
                    
    id_garagem1 = db_cadastrar_garagem(conexao, "Curitiba", 1)
    assert id_garagem1 == 1, "Erro: Primeira garagem deveria receber ID 1"

    try:
        db_cadastrar_garagem(conexao, "São Paulo", 999)
        assert False, "Erro: Permitida garagem vinculada a uma transportadora fantasma"
    except ValueError:
        pass


    print("[Testando]: Atualização de Cadastros")

    db_atualizar_transportadora(conexao, 1, "Alfa Logística S/A", "12345678901234")
    cursor.execute("SELECT nome_fantasia FROM transportadoras WHERE id = 1")
    assert cursor.fetchone()[0] == "Alfa Logística S/A", "Erro: O nome não foi atualizado no banco"

    try:
        db_atualizar_transportadora(conexao, 55, "Nome Qualquer", "9999")
        assert False, "Erro: Permitiu atualizar uma transportadora que não existe"
    except ValueError:
        pass



    print("[Testando]: Exclusão de Cadastros")

    db_excluir_transportadora(conexao, 1)

    cursor.execute("SELECT * FROM transportadoras WHERE id = 1")
    assert cursor.fetchone() is None, "Erro: Transportadora não foi excluída"

    cursor.execute("SELECT * FROM garagens WHERE id_transportadora = 1")
    assert cursor.fetchone() is None, "Erro: Garagem vinculada sobrou no banco (Dados órfãos)"

    try:
        db_excluir_transportadora(conexao, 1)
        assert False, "Erro: Permitiu excluir novamente um ID apagado"
    except ValueError:
        pass

    conexao.close()
    print("\n==================================================")
    print("  SUCESSO: Todos os asserts da prova passaram!    ")
    print("==================================================")

if __name__ == "__main__":
    executar_testes_prova()
