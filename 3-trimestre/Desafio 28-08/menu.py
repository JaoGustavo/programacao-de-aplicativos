import marca
import modelo
import veiculo

def menu_marcas():
    opcao = 0
    while opcao != 5:
        print("1. Cadastrar Marca")
        print("2. Listar Marcas")
        print("3. Alterar Marca")
        print("4. Excluir Marca")
        print("5. Voltar")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1: marca.cadastrar()
        elif opcao == 2: marca.listar()
        elif opcao == 3: marca.alterar()
        elif opcao == 4: marca.excluir()

def menu_modelos():
    opcao = 0
    while opcao != 5:
        print("1. Cadastrar Modelo")
        print("2. Listar Modelos")
        print("3. Alterar Modelo")
        print("4. Excluir Modelo")
        print("5. Voltar")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1: modelo.cadastrar()
        elif opcao == 2: modelo.listar()
        elif opcao == 3: modelo.alterar()
        elif opcao == 4: modelo.excluir()

def menu_veiculos():
    opcao = 0
    while opcao != 5:
        print("1. Cadastrar Veiculo")
        print("2. Listar Veiculos")
        print("3. Alterar Veiculo")
        print("4. Excluir Veiculo")
        print("5. Voltar")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1: veiculo.cadastrar()
        elif opcao == 2: veiculo.listar()
        elif opcao == 3: veiculo.alterar()
        elif opcao == 4: veiculo.excluir()

def menu_principal():
    opcao = 0
    while opcao != 4:
        print("1. Gerenciar Marcas")
        print("2. Gerenciar Modelos")
        print("3. Gerenciar Veiculos")
        print("4. Sair")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1:
            menu_marcas()
        elif opcao == 2:
            menu_modelos()
        elif opcao == 3:
            menu_veiculos()
        elif opcao == 4:
            print("Saindo do sistema")

if __name__ == "__main__":
    menu_principal()
