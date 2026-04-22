senha_correta = input ("Digite sua senha: ")
def validar_senha (senha, senha_correta):
    while senha != senha_correta:
        if senha <=6:
            print ("True")
        else:
            print ("False")
print ("Senha cadastrada com sucesso!")