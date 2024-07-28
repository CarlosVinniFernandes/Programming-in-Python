nome = str(input('Qual o seu nome?'))
nome2 = nome.upper()
if nome2 == 'GUSTAVO':
    print('Que nome bonito!')
elif nome2 == 'PAULO':
    print('Seu nome é legal')
else:
    print('Seu nome é tão normal')
print('Tenha um bom dia, {}!'.format(nome))

