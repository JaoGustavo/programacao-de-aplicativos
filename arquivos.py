lista_pendente = ["Relatorio.pdf", "Foto.png", "Planilha.xlsx"] 
print(f"lista atual: {lista_pendente}")
concluidos = [] 
concluidos.append(lista_pendente[0])
lista_pendente.pop(0)
print(f"lista atualizada: {lista_pendente}")