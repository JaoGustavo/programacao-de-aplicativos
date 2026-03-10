id = int(input("digite seu ID"))
temperatura = float(input("digite sua temperatura"))
tempo_de_uso = float(input("digite o tempo que a maquina esta funcionando"))

if (id % 3 == 0) and (temperatura > 40 or tempo_de_uso > 8):
    print:(f"Funcionario {id}, voce foi escalado para a ,manutençao preventina hoje")
else:
    print (f"Funcionário {id}, sua máquina opera dentro dos padrões normais.")