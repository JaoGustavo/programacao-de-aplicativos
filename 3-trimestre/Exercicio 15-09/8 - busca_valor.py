def busca_palavra(lista, palavra):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0
    
    while inicio <= fim:
        meio = (inicio + fim) // 2

        comparacoes = comparacoes + 1
        if lista[meio] == palavra:
            return meio, comparacoes

        comparacoes = comparacoes + 1
        if lista[meio] < palavra:
            inicio = meio + 1

        else:
            fim = meio - 1
            
    return -1, comparacoes


if __name__ == "__main__":
    palavras = ["abacaxi", "banana", "carro", "dado", "elefante", "faca", "gato"]

    encontrado, testes_1 = busca_palavra(palavras, "faca")
    print("Teste 1:")
    print("Palavra 'faca' encontrada no índice:", encontrado)
    print("Comparações realizadas:", testes_1)
    print("-" * 40)

    ausente, testes_2 = busca_palavra(palavras, "zebra")
    print("Teste 2:")
    print("Palavra 'zebra' encontrada no índice:", ausente)
    print("Comparações realizadas:", testes_2)
