import random
import sqlite3
import time

random.seed(42)
massa_dados = [random.randint(1, 10000) for _ in range(1000)]

def bubble_sort_benchmark(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

lista_teste_python = massa_dados.copy()

tempo_inicial_python = time.time()
bubble_sort_benchmark(lista_teste_python)
tempo_final_python = time.time() - tempo_inicial_python


conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE dados_benchmark (numero INTEGER)")
cursor.executemany("INSERT INTO dados_benchmark VALUES (?)", [(x,) for x in massa_dados])
conexao.commit()

tempo_inicial_sqlite = time.time()
cursor.execute("SELECT numero FROM dados_benchmark ORDER BY numero ASC")
resultados_banco = cursor.fetchall()
tempo_final_sqlite = time.time() - tempo_inicial_sqlite

conexao.close()

print(f"Tempo de Execução do Bubble Sort  {tempo_final_python:.6f} segundos")
print(f"Tempo de Execução do ORDER BY  {tempo_final_sqlite:.6f} segundos")