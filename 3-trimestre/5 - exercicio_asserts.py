def frete_gratis(valor):
    return valor >= 200

def pode_votar(idade):
    return idade >= 16

def senha_valida(senha):
    return len(senha) >= 8



assert frete_gratis(199.99) is False   # - F
assert frete_gratis(200) is True   # - P
assert frete_gratis(200.01) is True   # - P


assert pode_votar(15) is False   # - F
assert pode_votar(16) is True   # - P
assert pode_votar(17) is True   # - P


assert senha_valida("1234567") is False   # - F
assert senha_valida("12345678") is True   # - P
assert senha_valida("123456789") is True   # - P
