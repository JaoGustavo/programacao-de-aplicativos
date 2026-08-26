def classificar_idade(idade):
    if idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adulto"
    else:
        return "Adulto"

assert classificar_idade(10) == "Criança"  # - P
assert classificar_idade(15) == "Adolescente"  # - F
assert classificar_idade(18) == "Adulto"  # - P




def classificar_idade(idade):
    if idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    else:
        return "Adulto"


assert classificar_idade(10) == "Criança"  # - P
assert classificar_idade(15) == "Adolescente"  # - P
assert classificar_idade(18) == "Adulto"  # - P

# Estava errado porque a funcao mostrava "Adulto" e devia mostrar  "Adolescente"