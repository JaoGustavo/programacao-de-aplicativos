nome_de_usuario = input("digite o nome de usuario")
codigo_secreto = int(input("digite o codigo de segurança"))

if nome_de_usuario == "admin" and codigo_secreto == 999:
        print ("acesso ao servidor liberado. Sistema online")
else:
        print ("Falha na autenticaçao. Alerta de segurnaça ligado")