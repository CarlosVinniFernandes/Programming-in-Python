import random
pc = random.randint(1, 5)
us = int(input('Escolha um número de 1 a 5\n'))
print('O número escolhido foi: {}'.format(pc))
if pc == us:
    print('Você ganhou!')
else:
    print('Você perdeu!')
