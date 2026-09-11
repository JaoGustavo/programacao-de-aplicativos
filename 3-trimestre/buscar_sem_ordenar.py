matriculas = [502, 101, 999, 304, 205, 110]

print(f"Tentativa direta frustrada: A busca falha se aplicada em {matriculas}")

n_mat = len(matriculas)
for i in range(n_mat):
    min_idx = i
    for j in range(i + 1, n_mat):
        if matriculas[j] < matriculas[min_idx]:
            min_idx = j
    matriculas[i], matriculas[min_idx] = matriculas[min_idx], matriculas[i]

print(f"Lista de matrículas devidamente padronizada e ordenada: {matriculas}")

def busca_binaria_posicao(lista, alvo):
    esq = 0
    dir = len(lista) - 1
    
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    return -1

posicao_resultado = busca_binaria_posicao(matriculas, 205)
print(f"Matrícula 205 localizada com total sucesso na posição de índice: {posicao_resultado}")