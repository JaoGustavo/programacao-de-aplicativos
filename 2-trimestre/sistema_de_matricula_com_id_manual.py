import json 
import os 

DADOS_BANCO = "escola.json"

def cadastrar():
    if os.path.exists(DADOS_BANCO): 
        with open(DADOS_BANCO, 'r', encoding='utf-8') as f: 
            escola = json.load(f)
    else:
        i = [] 
    novo_item = {
        "id": int(input("Digite seu ID: ")),
        "nome": input("Nome Completo: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    }

    dados.append(novo_item)

    with open(DADOS_BANCO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False) 
        
    print("ID salvo com sucesso!") 

cadastrar()