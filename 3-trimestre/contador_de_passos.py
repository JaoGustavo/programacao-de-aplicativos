def busca_sequencial(lista, alvo):
    comparacoes = 0
    for elemento in lista:
        comparacoes += 1
        if elemento == alvo:
            return comparacoes
    return comparacoes

def busca_binaria(lista, alvo):
    comparacoes = 0
    esquerda = 0
    direita = len(lista) - 1
    
    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return comparacoes
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return comparacoes

numeros = list(range(1, 101))

resultado_sequencial = busca_sequencial(numeros, 95)
resultado_binaria = busca_binaria(numeros, 95)

print(f"Comparações na Busca Sequencial: {resultado_sequencial}")
print(f"Comparações na Busca Binária: {resultado_binaria}")