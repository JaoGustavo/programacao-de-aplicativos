def encontrar_maior_sequencial(vetor):
    if not vetor:
        return None, -1

    maior_valor = vetor[0]
    posicao_maior = 0

    for indice in range(1, len(vetor)):
        if vetor[indice] > maior_valor:
            maior_valor = vetor[indice]
            posicao_maior = indice
            
    return maior_valor, posicao_maior
meu_vetor = [12, 45, 78, 2, 34, 99, 51, 8, 23, 67]

maior, posicao = encontrar_maior_sequencial(meu_vetor)

print(f"O maior número é o {maior} e ele está na posição/índice {posicao}.")
