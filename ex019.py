import random
a = str(input('Escolha o 1o aluno'))
b = str(input('Escolha o 2o aluno'))
c = str(input('Escolha o 3o aluno'))
d = str(input('Escolha o 4o aluno'))
alunos = [a, b, c, d]
escolhido = random.choice(alunos)
print('O aluno escolhido foi o {}'.format(escolhido))