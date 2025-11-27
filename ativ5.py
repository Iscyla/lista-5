#Crie uma tupla com 6 cidades. Depois exiba:• A primeira cidade • A última cidade • Quantas cidades existem • Todas as cidades uma por linha

cidades = ("Losagenles", "Vitória", "Paris", "Tóquio", "Bangkok", "Istambul")

print(f"\nA primeira cidade é: {cidades[0]}\n")
print(f"A última cidade é: {cidades[5]}")
print("\nTodas as cidades:")
for cidade in cidades:
    print(cidade)