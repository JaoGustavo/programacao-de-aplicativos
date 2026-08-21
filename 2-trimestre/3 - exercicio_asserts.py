def calcular_desconto(preco, percentual):
    return preco - percentual


assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45




# Correção da função:
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


# Depois da correção, todos devem PASSAR.
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45