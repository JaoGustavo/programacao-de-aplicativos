senha = input("Digite sua senha: ")
tentativa = int(input("Qual é o numero da tentativa atual? "))
token = input("voce possui o token? (s/n)")

if (senha == "admin123") and (tentativa % 3 == 0 or token == "s"):
    print(f"Tentativa nº {tentativa}: ACESSO CONCEDIDO.")
else:
    print(f"Tentativa nº {tentativa}: ACESSO BLOQUEADO POR PROTOCOLO.")
