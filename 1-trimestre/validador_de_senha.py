def senha_valida(senha):
    return len(senha) >= 6

print("Cadastro de Senha")

entrada = input("Digite uma senha (mínimo 6 caracteres): ")

if senha_valida(entrada):
    print("Senha cadastrada com sucesso!")
else:
    print("Senha muito curta!")