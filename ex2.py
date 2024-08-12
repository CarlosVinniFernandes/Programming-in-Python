nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

if nome and idade:
    print(f'Seu nome é {nome}\nSeu nome invertido é {nome[::-1]}\nSeu nome tem {len(nome)}')
    if ' ' in nome: print('Seu nome tem espaço')
    else: print('Seu nome n tem espaço')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra é {nome[len(nome)-1:]}')

else:
    print('Voce esqueceu de digitar algo')