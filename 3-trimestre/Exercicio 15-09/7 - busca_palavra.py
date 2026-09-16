def busca_palavra(lista, palavra_alvo):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista[meio] == palavra_alvo:
            return meio
        
        if lista[meio] < palavra_alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return -1


dicionario = ["abacaxi", "banana", "carro", "dado", "elefante", "faca"]

print(busca_palavra(dicionario, "dado"))
print(busca_palavra(dicionario, "abacate"))