sal = float(input('Qual o seu salário?\n'))
if sal > 1250:
    novosal = sal + (sal*10/100)
    print('Seu novo salário será de {}R$'.format(novosal))
else:
    novosal2 = sal + (sal * 15 / 100)
    print('Seu novo salário será de {}R$'.format(novosal2))