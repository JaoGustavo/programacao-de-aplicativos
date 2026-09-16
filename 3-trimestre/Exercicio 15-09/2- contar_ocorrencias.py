def contar_sequencial(lista, alvo):
    contador = 0

    for elemento in lista:
        if elemento == alvo:
            contador = contador + 1
            
    return contador

minha_lista = [5, 7, 3, 7, 8, 1, 7, 9, 2, 4]
numero_procurado = 7

total_vezes = contar_sequencial(minha_lista, numero_procurado)

print(f"O número {numero_procurado} aparece {total_vezes} vezes na lista.")
