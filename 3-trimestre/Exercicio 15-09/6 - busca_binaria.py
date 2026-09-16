def busca_binaria(vetor, item):
    ini = 0
    fim = len(vetor) - 1
    
    while ini <= fim:
        meio = (ini + fim) // 2
        
        if vetor[meio] == item:
            return meio
        
        if vetor[meio] < item:
            ini = meio + 1
        else:
            fim = meio - 1
            
    return -1


lista = [10, 20, 30, 40, 50, 60]

print(busca_binaria(lista, 40))
print(busca_binaria(lista, 15))
