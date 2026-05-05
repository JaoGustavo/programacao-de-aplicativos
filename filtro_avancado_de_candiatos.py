def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    aprovado = False
    if (nota < 80 or anos_xp > 2) or possui_certificacao == "S":
        aprovado = True
    if aprovado == True: 
        print("Contratado!")
    elif aprovado != True:
        print("Descartar")

nota = float(input(  "Digite sua nota: "))
anos = int(input("Digite seus anos de experiencia: "))
certificado = input("possui certificado? (S/N): ")

verificar_aprovacao(nota, anos, certificado)