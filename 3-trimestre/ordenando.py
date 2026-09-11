alunos = ["Pedro", "Ana", "Lucas", "Beatriz", "Carlos"]

def bubble_sort_nomes(lista):
    n = len(lista)
    arr = lista.copy()
    
    print(f"Estado inicial da lista de alunos: {arr}\n")

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"Troca efetuada: [{arr[j + 1]}] mudou de lugar com [{arr[j]}] -> {arr}")
    return arr

alunos_ordenados = bubble_sort_nomes(alunos)
print(f"\nLista final completamente ordenada em ordem alfabética: {alunos_ordenados}")