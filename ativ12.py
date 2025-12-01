#• Peça nome 
#• Peça idade 
#• Peça cidade 
#• Retorne um dicionário com esses dados

def cadastrar_pessoa():
    nome = input("\nNome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")
    
    return {
        "nome": nome,
        "idade": idade,
        "cidade": cidade }

cadastros = []

#• Use um while para cadastrar várias pessoas
#• Cada pessoa deve ser guardada dentro de uma lista de dicionários
#• Pare quando o usuário digitar “sair”
#• Ao final, exiba todos os cadastros organizados

while True:
    opcao = input("\nDigite ENTER para cadastrar ou 'sair' para encerrar: ").lower()
    if opcao == "sair":
        break
    
    pessoa = cadastrar_pessoa()
    cadastros.append(pessoa)

print("\nLista de Cadastros: ")
for i, p in enumerate(cadastros, start=1):
    print(f"  Nome: {p['nome']}")
    print(f"  Idade: {p['idade']}")
    print(f"  Cidade: {p['cidade']}")
