
def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"



assert situacao_aluno(8) == "Aprovado"  # - P
assert situacao_aluno(6) == "Aprovado"  # - P
assert situacao_aluno(5.9) == "Reprovado"  # - P
assert situacao_aluno(0) == "Reprovado"  # - P
assert situacao_aluno(10) == "Aprovado"  # - P


assert situacao_aluno(-1) == "Reprovado"


# 6 e 5.9 são casos de limite porque ficam no limite da aprovação.
# 6 é o mínimo para aprovação e 5.9 está logo abaixo.
# Teste extra: -1, para verificar uma média abaixo de zero.
