def analisar_vendas(nome, lista_vendas, meta_mensal):
    media = sum(lista_vendas) / len(lista_vendas)
    
    bateu_meta = "bateu" if media >= meta_mensal else "não bateu"
    
    return f"O vendedor {nome} teve média de {media:.2f} e {bateu_meta} a meta"

resultado = analisar_vendas("Carlos", [1200, 1500, 1100, 1900], 1400)
print(resultado)