autorizados = ["Alice", "Bob", "Carlos"]
nome = input("digite o nome do pesquisador")

if nome in autorizados:
    print(f"Acesso Permitido! O pesquisador {nome} está na posição {indice}.")

    remover = input("Deseja remover esse pesquisador da lista? (s/n): ")
    if remover.remove() == "s"
