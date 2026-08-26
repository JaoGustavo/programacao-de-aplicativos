def buscar_nome(lista, nome):
    return nome in lista
 
 
def tem_senha_valida(senha):
    return len(senha) >= 8
 
 

assert buscar_nome([], "Ana") is False
assert buscar_nome(["Ana", "Bruno", "Carla"], "Bruno") is True
assert buscar_nome(["João", "Maria", "Pedro"], "Lucas") is False
assert tem_senha_valida("") is False
assert tem_senha_valida("12345678") is True
assert tem_senha_valida("1234567") is False
 
print("Todos os testes passaram.")
