lista = [2, 5, 7, 10, 15]
novo_numero = 8

inicio = 0
fim = len(lista)

while inicio < fim:
    meio = (inicio + fim) // 2
    
    if lista[meio] < novo_numero:
        inicio = meio + 1
    else:
        fim = meio

lista.insert(inicio, novo_numero)

print(f"Lista atualizada: {lista}")
print(f"O número foi inserido na posição: {inicio}")
