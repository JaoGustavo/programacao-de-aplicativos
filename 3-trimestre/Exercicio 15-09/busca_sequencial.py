def busca_sequencial(vetor, alvo):
    for indice in range(len(vetor)):
        if vetor[indice] == alvo:
            return indice
            
    return -1

meu_vetor = [12, 45, 7, 9, 23, 56, 89, 34, 1, 90]
numero_procurado = 23

resultado = busca_sequencial(meu_vetor, numero_procurado)

if resultado != -1:
    print(f"O número {numero_procurado} foi encontrado no índice {resultado}.")
else:
    print(f"O número {numero_procurado} não está no vetor.")
