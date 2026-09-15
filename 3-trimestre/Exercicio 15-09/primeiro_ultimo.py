def buscar_limites(vetor, alvo):
    primeira = -1
    ultima = -1
    
    for i in range(len(vetor)):
        if vetor[i] == alvo:
            if primeira == -1:
                primeira = i
            ultima = i
            
    return primeira, ultima

dados = [2, 5, 3, 5, 8, 5, 1]
numero = 5

ini, fim = buscar_limites(dados, numero)

if ini != -1:
    print(f"Primeira posição: {ini} | Última posição: {fim}")
else:
    print("Número não encontrado.")
