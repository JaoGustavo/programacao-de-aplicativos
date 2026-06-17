livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []

livro = input("digite o nome do livro que deseja: ")

if livro in livros_disponiveis:
    livros_disponiveis.remove(livro)
    livros_emprestados.append(livro)
    print ("Empréstimo realizado com sucesso!")
else:
    print("Desculpe, este livro não está no acervo.")


livro_emprestado = input("Digite o nome do livro para devolução: ")
if livro_emprestado in livros_emprestados:
    livros_emprestados.remove(livro_emprestado)
    livros_disponiveis.append(livro_emprestado)
    print("Livro devolvido com sucesso!")
else:
    print("Este livro não é emprestado.")

del livros_disponiveis[0:2]
print (f"Estado final das duas listas: {livros_disponiveis} e lista do emprestimo: {livros_emprestados}")