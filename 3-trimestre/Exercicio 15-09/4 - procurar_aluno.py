def buscar_aluno(lista, nome_procurado):
    for aluno in lista:
        if aluno.lower() == nome_procurado.lower():
            return True
    return False

alunos = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
nome = "Diana"

if buscar_aluno(alunos, nome):
    print(f"O aluno {nome} foi encontrado!")
else:
    print(f"O aluno {nome} não foi encontrado.")
