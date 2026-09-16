vetor = [i * 2 for i in range(1, 101)]

def busca_sequencial(vetor, alvo):
    comparacoes = 0
    for i in range(len(vetor)):
        comparacoes += 1
        if vetor[i] == alvo:
            return comparacoes
        elif vetor[i] > alvo:
            return comparacoes
    return comparacoes

def busca_binaria(vetor, alvo):
    comparacoes = 0
    inicio = 0
    fim = len(vetor) - 1
    
    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        if vetor[meio] == alvo:
            return comparacoes
        elif vetor[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return comparacoes

valores_teste = [10, 110, 155]

for valor in valores_teste:
    comp_seq = busca_sequencial(vetor, valor)
    comp_bin = busca_binaria(vetor, valor)
    
    print(f"Buscando {valor}:")
    print(f"Sequencial fez {comp_seq} comparações")
    print(f"Binária fez {comp_bin} comparações\n")
