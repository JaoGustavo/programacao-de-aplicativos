usuario = input("qual seu usuario")
senha = int(input("insira a senha"))

if (usuario == "admin" or usuario == "root") and senha == 1234:
    print ("acesso liberado")
else:
    print("acesso negado")
