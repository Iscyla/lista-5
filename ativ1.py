#Repetição – Crie um programa que peça um número ao usuário e conte de 1 até esse número, exibindo todos os valores.

num = int(input("Informe um número para a contagem: "))
i = 0
while i <= num:
    print(f"{num} + {i} = {num+i}")
    i += 1

print("Fim do programa!")