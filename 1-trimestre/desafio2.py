cargo = input("digite seu cargo: ")
codigo = int(input("digite o codigo de acesso: "))
botao = input("botao de emergencia acionado? (s/n): ")
epi = input("EPI completo (s/n): ")
 
if (cargo == "ENGENHEIRO" or "TECNICO") and (codigo == 1234 or botao == "s") and epi == "s":
    print ("Acesso Liberado!")
else:
    print ("Acesso Negado!")