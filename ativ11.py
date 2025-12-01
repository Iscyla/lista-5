#• Peça 4 notas ao usuário
#• Coloque numa lista
#• Use a função para calcular a média
#• Exiba o resultado

def calcular_media(lista_notas):

    for nota in lista_notas:
        float(input("Digite sua nota: "))
        lista_notas.append(nota)

        media = nota / len(lista_notas)

    print(f"A média das notas é: {media:.2f}")
