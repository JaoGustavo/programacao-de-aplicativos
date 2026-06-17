ferramentas = ["Chave Inglesa", "Alicate", "Martelo", "Parafusadeira"]
procurando = input("Digite a ferramenta que está procurando: ")

for ferramenta in ferramentas:
    if procurando == ferramenta:
        print(f"Peça encontrada na posição {indice}!")
while procurando != ferramentas:
    ferramenta = input("Deseja adicionar nova ferramenta?: ")
