def pode_votar(idade):
    return idade >= 16


assert pode_votar(15) == False
assert pode_votar(16) == True
assert pode_votar(30) == True
assert pode_votar(17) == True


