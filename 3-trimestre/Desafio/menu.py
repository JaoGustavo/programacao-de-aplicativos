import cursos
import alunos

def menu():
    opcao = 0
    while opcao != 3:
        print("1. Cursos")
        print("2. Alunos")
        print("3. Sair")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1:
            cursos.menu_cursos()
        elif opcao == 2:
            alunos.menu_alunos()
        elif opcao == 3:
            print("Saindo")

menu()
