import sqlite3 

def cadastrar():
    try:
        conexao = sqlite3.connect ('escola.db') 
        cursor = conexao.cursor() 
        cursor.execute ('''CREATE TABLE IF NOT EXISTS alunos ( 
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            telefone TEXT,             
                            turma TEXT,
                            idade INTEGER,
                            cidade TEXT,
                            endereco TEXT,
                            estado TEXT,
                            cpf TEXT UNIQUE NOT NULL 
                            )''') 


        nome_aluno = input("NOME: ") 
        telefone_aluno = input("TELEFONE: ") 
        turma_aluno = input("TURMA: ") 
        idade_aluno = int(input("IDADE: "))
        CPF_aluno = input("CPF: ")
        cidade_aluno = input("CIDADE: ") 
        endereco_aluno = input("ENDERECO: ")
        estado_aluno = input("ESTADO: ") 
       
        comando_inserir = (f''' 
                            INSERT into alunos (nome, telefone, turma, idade, cpf, cidade, endereco, estado)
                            VALUES('{nome_aluno}','{telefone_aluno}','{turma_aluno}','{idade_aluno}','{CPF_aluno}','{cidade_aluno}','{endereco_aluno}','{estado_aluno}',''') 
                                
        cursor.execute(comando_inserir) 
        conexao.commit()

    except ValueError:
        print("valor invalido")
    except TypeError:
        print("tipo de dado invalido") 
    except ZeroDivisionError:
        print("arquivo não encontrado")
    except FileNotFoundError:
        print("divisão por zero")	
    except Exception as erro:
        print(f"ocorreu um erro: {erro}")	
    finally:
            conexao.close 


def listar():
    try:
        conexao = sqlite3.connect ('escola.db') 
        cursor = conexao.cursor() 

        cursor.execute("SELECT * FROM alunos") 
        todos_alunos = cursor.fetchall()

        for aluno in todos_alunos: 
            print(f"ID: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Telefone: {aluno[2]}")
            print(f"Turma: {aluno[3]}")
            print(f"Idade: {aluno[4]}")
            print(f"CPF: {aluno[5]}")
            print(f"cidade: {aluno[6]}")
            print(f"endereco: {aluno[7]}")
            print(f"estado: {aluno[8]}")
            print("-" * 30)
    except ValueError:
        print("valor invalido")
    except TypeError:
        print("tipo de dado invalido") 
    except ZeroDivisionError:
        print("arquivo não encontrado")
    except FileNotFoundError:
        print("divisão por zero")	
    except Exception as erro:
        print(f"ocorreu um erro: {erro}")	
    finally:
        print("codigo encerrado")



def alterar():
    try:
        listar()

        conexao = sqlite3.connect ('escola.db') 
        cursor = conexao.cursor() 


        id_aluno = int(input("Qual é o teu ID: "))
        
        cursor.execute(f'''SELECT * FROM alunos WHERE id = {id_aluno}''')
        alunos = cursor.fetchone()

        if not id_aluno:
            print("Não encontrado!")
        else:
            novo_nome = input("qual o novo nome: ")
            novo_telefone = input("qual o novo telefone: ")
            novo_turma = input("qual a nova turma: ")
            novo_idade = int(input("qual a nova idade: "))
            novo_cpf = input("qual o novo cpf: ")
           

            comando = f'''UPDATE alunos SET nome = '{novo_nome}',telefone = '{novo_telefone}',materia = '{novo_turma}',idade = '{novo_idade}',cpf = '{novo_cpf}','''
            
            conexao.commit()
            
    except ValueError:
        print("valor invalido")
    except TypeError:
        print("tipo de dado invalido") 
    except ZeroDivisionError:
        print("arquivo não encontrado")
    except FileNotFoundError:
        print("divisão por zero")	
    except Exception as erro:
        print(f"ocorreu um erro: {erro}")	
    finally:
        print("codigo encerrado")
        conexao.close 


def deletar():
    try:
        conexao = sqlite3.connect("escola_demonstracao.db")
        cursor = conexao.cursor()

        listar()

        id_alunos = int(input(" Qual ID deseja deletar: " ))

        cursor.execute(f'''DELETE FROM alunos WHERE Id = {id_alunos}''')

        conexao.commit()
        print("aluno deletado")
    except ValueError:
        print("valor invalido")
    except TypeError:
        print("tipo de dado invalido") 
    except ZeroDivisionError:
        print("arquivo não encontrado")
    except FileNotFoundError:
        print("divisão por zero")	
    except Exception as erro:
        print(f"ocorreu um erro: {erro}")	
    finally:
        print("codigo encerrado")
        conexao.close 

       



def menu():
    try:
      
        while True:
            print("\n--- TABELA ALUNOS ---")
            print("\n=== SISTEMA ESCOLAR ===")  
            print("1. Cadastrar alunos") 
            print("2. Listar alunos") 
            print("3. Atualizar alunos") 
            print("4. Excluir alunos") 
            print("5. Sair")
                
            opcao = input("Escolha uma opção: ")

            if opcao == '1': cadastrar()
            elif opcao == '2': listar() 
            elif opcao == '3': alterar() 
            elif opcao == '4': deletar() 
            elif opcao == '5': break
            else: print("Opção inválida!")
            
    except ValueError:
        print("valor invalido")
    except TypeError:
        print("tipo de dado invalido") 
    except ZeroDivisionError:
        print("arquivo não encontrado")
    except FileNotFoundError:
        print("divisão por zero")	
    except Exception as erro:
        print(f"ocorreu um erro: {erro}")	
    finally:
        print("codigo encerrado")

menu()
