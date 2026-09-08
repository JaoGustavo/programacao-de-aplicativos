def dobrar(numero):
    return numero * 2

assert dobrar(3) == 6          # P - passsa
assert dobrar(0) == 1          # F - falha         
assert dobrar(-2) == -4        # P - passsa



# O assert que falhou foi: assert dobrar(0) == 1. o resultado foi 0.
# A expectativa estava incorreta porque a função dobrar()
# multiplica o número por 2:   0 * 2 = 0
# O resultado esperado deveria ser 0, e não 1.