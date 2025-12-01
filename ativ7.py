#Crie um menu usando match case:
#1 - Olá
#2 - Informações
#3 - Sair
#Dependendo da escolha, exiba uma mensagem adequada.

def menu():
    print("Menu de alguma coisa")
    print("1 - Olá!")
    print("2 - Informações!")
    print("3 - sair!")

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
    