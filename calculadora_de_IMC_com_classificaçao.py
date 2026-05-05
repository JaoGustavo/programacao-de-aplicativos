def gerar_relatorio_saude(nome, peso, altura, idade):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        categoria = "Peso normal"
    elif 25 <= imc <= 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    return f"Olá {nome}! Com {idade} anos, seu IMC é {imc} e sua classificação é: {categoria}."

print("      Calculadora de Saúde       ")
nome_usuario = input("Digite seu nome: ")
peso_usuario = float(input("Digite seu peso kg: "))
altura_usuario = float(input("Digite sua altura: "))
idade_usuario = int(input("Digite sua idade: "))

relatorio = gerar_relatorio_saude(nome_usuario, peso_usuario, altura_usuario, idade_usuario)
print("\nRelatório Final:")
print(relatorio)