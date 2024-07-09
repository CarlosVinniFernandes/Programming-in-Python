import random
aluno1 = str(input('Coloque o nome de um aluno:'))
aluno2 = str(input('Coloque o nome de um aluno:'))
aluno3 = str(input('Coloque o nome de um aluno:'))
aluno4 = str(input('Coloque o nome de um aluno:'))
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('A ordem será:', alunos)