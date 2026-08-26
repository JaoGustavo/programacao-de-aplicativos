def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

assert calcular_media(7, 8, 9) == 8
assert calcular_media(10, 10, 10) == 10
assert calcular_media(5, 6, 7) == 6