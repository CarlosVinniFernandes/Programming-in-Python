tamanho = int(input('Que tamanho voce quer sua arvore?'))
espaco = tamanho-1
for i in range(1, tamanho+1):
    print('\t' * (10), end='')
    print(' '*espaco, end='')
    print(' #' * i)
    espaco -=1