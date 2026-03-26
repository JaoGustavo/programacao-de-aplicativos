compras = []
produtos = input("Digite seu produto: ")

while produtos != "fim":
    compras = compras + [produtos]
    produtos = input("Digite o nome de um produto (ou 'fim' para fializar a compra): ")

print("Lista d produtos: ")
for item in compras:
    print(f"{item}")
