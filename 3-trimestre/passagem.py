idades = [17, 11, 15, 13, 12]

def selection_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(n):
        indice_minimo = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j

        if indice_minimo != i:
            arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]
            
    return arr

idades_ordenadas = selection_sort(idades)
print(f"Lista final de idades ordenada de forma crescente: {idades_ordenadas}")