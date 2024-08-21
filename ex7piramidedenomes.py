tamanho = input('Escolha o tamanho da arvore: ')
nome = len(tamanho)
espaco = nome - 1

for t in range(0, nome):
    print("\t", end="")

    for i in range(espaco):
        print(" ", end="")

    for j in range(nome, espaco, -1):
        print(f'{j} ', end='')

    print("")
    espaco -= 1
