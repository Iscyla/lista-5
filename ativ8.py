#Dicionário – Crie um dicionário com os seguintes campos:• Nome • Idade • Curso Peça os valores ao usuário e ao final exiba o dicionário completo formatado.

pessoa = {}

pessoa["nome"] = input("Digite o nome: ")
pessoa["idade"] = int(input("Digite a idade: "))
pessoa["curso"] = input("Digite o curso: ")

for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")