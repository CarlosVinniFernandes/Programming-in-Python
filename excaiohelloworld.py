import random
import time
#palavra = input('Digite uma palavra')
palavra = 'hello world'
letras = 'abcdefghijklmnopqrstuvwxyz '
letra_sorteada = random.choice(letras)
j=0
palavra_formada = ''
i=0
espaco = 1
for j in range (len(palavra)):
    while letra_sorteada != palavra[j]:
        letra_sorteada = random.choice(letras)
        palavra_formada += letra_sorteada
        print(f'{palavra_formada}')
        time.sleep(0.05)

        if letra_sorteada == palavra[i]:
            i+=1
        else:
            palavra_formada = palavra_formada[:-1]
            continue

