def situacao_faltas(faltas):
    if faltas <= 4:
        return "Regular"
    elif faltas <= 10:
        return "Atenção"
    else:
        return "Reprovado por falta"


assert situacao_faltas(0) == "Regular"   # - P
assert situacao_faltas(4) == "Regular"   # - P
assert situacao_faltas(5) == "Atenção"   # - P
assert situacao_faltas(10) == "Atenção"   # - P
assert situacao_faltas(11) == "Reprovado por falta"   # - P