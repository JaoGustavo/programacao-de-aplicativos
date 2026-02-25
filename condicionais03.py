compra = float( input("digite o valor total da compra"))
cupom = input("digite o nome do cupom: ")


desconto = compra * 0.10
valor_desconto = compra - desconto

if cupom =="DEV10":
    print ("cupom válido", valor_desconto)
else:
    print("cupom invalido", compra)