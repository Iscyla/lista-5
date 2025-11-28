#Dicionário – Crie um dicionário com 3 produtos e seus preços. 
#Depois permita ao usuário digitar o nome de um produto e mostre seu preço. Se não existir, exiba “Produto não cadastrado”

produto = [{"nome":"café", "preco":25.95,},
            {"nome":"refrigerante", "preco":2.99,},
            {"nome":"Sabão em pó", "preco":17.99},
            {"nome":"pão", "preco":7.99}]

print("___Lista de Produtos___")
for i in produto:
    for chave, valor in i.items(): #Serve para pegar chave e valor dentro do dicionário
        print(f"{chave}:{valor}")

escolha = input("Informe um produto disnponível: ")

if escolha in produto: 
    print(f"Este produto se encontra dísponivel no preço {produto[escolha]}: ")

else:
    print(f"Produto não encontrado!")