#Com uma lista contendo 8 frutas, peça ao usuário uma fruta e diga se ela está na lista usando operador in.

frutiferas=["Manga", "Banana", "Uva", "Melancia", "Laranja", "Maça", "Limão", "Abacate", "Ameixa"]

fruta = (input("Informe o nome da fruta que deseja: "))

if fruta in frutiferas:
    print(f"A fruta {fruta} se encontra no nosso estoque!")

else:
    print(f"A fruta {fruta} não se encontra no nosso estoque!")

