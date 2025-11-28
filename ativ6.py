numero = (10, 20, 30, 40, 50, 60, 70, 80, 90, 10)

num = int(input("Digite um número: "))

if num in numero:
    print(f"O número {num} está na tupla.")
    print(f"\nO número {num} está no indice {numero.index(num)}.")
else:
    print(f"O número {num} não está na tupla.")