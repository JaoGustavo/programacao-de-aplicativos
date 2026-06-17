media = float(input("qual a sua media"))
renda = float(input("qual a sua renda"))
escola = input ("voce veio de escola publica? (s/n):")

if media >= 8.0 and renda <2.000 or escola == "s":
    print ("voce ganhou a bolsa ")
else:
    print ("voce nao obteve a bolsa")