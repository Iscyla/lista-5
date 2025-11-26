#Repetição – Peça 5 números ao usuário usando um for e mostre:• A soma total • A média dos números

print("Informe 5 números para a soma:\n")

soma=0

for i in range(1, 6):
    num = int(input(f"Informe o {i} número: "))
    soma += num 
    media = soma / 5

print(f"O resultado da somas é: {soma}")
print(f"A média é igual: {media}")

