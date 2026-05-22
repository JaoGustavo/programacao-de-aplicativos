import json # salva os dados
import os # verificase  o codigo existe 

BANCO_DADOS = 'alunos.json' #coloca o nome do arquivo 

def cadastrar(): #serve para cadastrar 
    print("\n--- Novo Cadastro ---")
    
    if os.path.exists(BANCO_DADOS): # verifica se o arquivo exiate 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo para ler 
            alunos = json.load(f) # converte em uma lista
    else:
        alunos = [] # se ele nao existir cria um novo 

    novo_aluno = { # cria um novo pelos dados digitados pela pessoa 
        "nome": input("Nome: "), #pede o nome 
        "telefone": input("Telefone: "), #pede o telefone 
        "turma": input("Turma: "), #pede a turma 
        "idade": int(input("Idade: ")),#pede a idade
        "cpf": input("CPF: ") #pede o CPF
    }
    
    alunos.append(novo_aluno) #adiciona o novo aluno na lista

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #salva os arquivos ja atualizados 
        json.dump(alunos, f, indent=4, ensure_ascii=False) #salva tudo no JSON
        
    print("Aluno cadastrado com sucesso!") 

def listar(): #serve para listar 
    print("\n--- Lista de Alunos ---") 
    
    if os.path.exists(BANCO_DADOS): # verifica se o arquivo existe
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo 
            alunos = json.load(f)  #carrega os dados 
    else:
        alunos = [] #se ele nao existir cria um novo

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return #ecerra a funcao 

    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")  #imprime os dados dos alunos da lista 

def atualizar():  #serve para atualizar 
    print("\n--- Atualizar Aluno ---")  
    if not os.path.exists(BANCO_DADOS): #verifica se os dados existem 
        print("Nenhum aluno cadastrado no sistema.")
        return #ecerra a funcao 

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo em formato de leitura 
        alunos = json.load(f) #converte em variavel
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ") # busca o cpf do aluno 
    
    for aluno in alunos: #procura o aluno na lista 
        if aluno['cpf'] == cpf_busca:
            print(f"Editando dados de: {aluno['nome']}") # mostra o nome do aluno q vai ser editado 
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # mostra o nome do aluno adicionado 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] #mostra o telefone novo
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] # motra n0va turma 
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) #mostra nova idade 
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] #mostra novo cpf 
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #salva no arquivo 
                json.dump(alunos, f, indent=4, ensure_ascii=False) 
            print("Dados atualizados com sucesso!")
            return #ecerra a funcao 
            
    print("Aluno não encontrado.")

def excluir(): #serve para excluir 
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(BANCO_DADOS): #verifica se o arquivo existem 
        print("Nenhum aluno cadastrado no sistema.")
        return #ecerra a funcao 

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo 
        alunos = json.load(f) # carrega os alunos 
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ") # mostra o cpf q sera removido 
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca] # cria uma nova lista sem o aluno removido 
    
    if len(nova_lista) < len(alunos): #verifica se alguem foi removido 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #salva a nova lista 
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) #
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu(): #funcao principal 
    if not os.path.exists(BANCO_DADOS): #verifica se o arquivo existe 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True: #mostra as opcoes 
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")  # Pede uma opção
        
        if opcao == '1': cadastrar() # Chama a função de cadastro
        elif opcao == '2': listar() # Chama a função de listagem 
        elif opcao == '3': atualizar() # Chama a função de atualização
        elif opcao == '4': excluir() # Chama a função de exclusão
        elif opcao == '5': break  # Fecha o programa
        else: print("Opção inválida!")   # Caso a opção seja inválida

menu() #inicia o sistema