def menu():
    print("=== MENU DE SEI LÁ ===")
    print("1 - Olá")
    print("2 - informações")
    print("3 - sair")

def ola():
    print("Olá, mundo!")

def informacoes():
    print("tem nada não palhaço kkkkkkkkk")

def sair():
    print("Saindo do programa...")


while True:
    menu()
    
    opcao = input("Esolha uma opção: ")

    match opcao:
    
        case "1":
            ola()
        case "2":
            informacoes()
        case "3":
            sair()
            break
        case _:
            print("Opção inválida! Tente novamente.")
    