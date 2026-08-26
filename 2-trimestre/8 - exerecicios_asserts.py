def pode_votar(idade):
    return idade >= 16


assert pode_votar(15) is False, "Esperado: False (15 anos não pode votar)"
assert pode_votar(16) is True, "Esperado: True (16 anos já pode votar)"
assert pode_votar(30) is True, "Esperado: True (30 anos pode votar)"
assert pode_votar(17) is True, "Esperado: True (17 anos pode votar)"

print("Todos os testes passaram como previsto.")
