def calcular_area(largura, comprimento):
    return largura * comprimento

contador = 1
while contador <= 3:
    print(f"Terreno {contador}")
    largura = float(input("Largura: "))
    comprimento = float(input("Comprimento: "))
    
    area = calcular_area(largura, comprimento)
    print(f"A área do terreno {contador} é: {area}")
    
    contador += 1 