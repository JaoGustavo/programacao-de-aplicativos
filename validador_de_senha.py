def senha_valida(senha):
    return len(senha) >= 6
    
print("--- Cadastro de Senha ---")

foi_cadastrada = False

while not foi_cadastrada:
    entrada = input("Digite uma senha (mínimo 6 caracteres): ")
    
    if senha_valida(entrada):
        print("Senha cadastrada com sucesso!")
        foi_cadastrada = True
    else:
        print("Senha muito curta! Tente novamente.")