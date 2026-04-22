nota = float(input("digite sua nota de 0  10: "))
def avaliar_desempenho (nota):
    if nota  >= 9:
      return  "Excelente"

    elif nota >= 7 :
     return "Bom"

    elif nota > 5 :
      return "Regular"

    else:
        return "Insuficiente"

print (avaliar_desempenho(nota))