ano = int(input('Que ano você quer saber?'))
div = ano%4
if div == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')