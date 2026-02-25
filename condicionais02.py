ataque = int(input("digite o dano do ataque do heroi"))
defesa = int(input("digite a defesa do vilao"))

dano = ataque - defesa 

if ataque <= defesa:
    print ("O vilão bloqueou o ataque!",dano)
elif ataque >= defesa:
    print ("ataque critico! voce causou dano ao vilao, o dano causado foi",dano)
