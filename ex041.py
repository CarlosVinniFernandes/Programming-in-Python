#from datetime import date
#atual = date.today().year
ano = int(input('Em que ano você nasceu?'))
idade = 2024 - ano

if idade <= 9:
    print('Você está na categoria mirim!')
elif idade > 9 and idade <= 14:
    print('Você está na categoria infantil!')
elif idade > 14 and idade <= 19:
    print('Você está na categoria junior!')
elif idade > 19 and idade <= 20:
    print('Você está na categoria sênior!')
else:
    print('Você está na categoria master!')

