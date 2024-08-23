#Sequência de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
termos = int(input('Digite a quantidade de termos que você quer: '))
termo1 = 0
termo2 = 1
contador = 0

if termos == 1:
    print(termo1)

while contador < termos:
    print(f' {termo1} ',end='')
    soma = termo1 + termo2
    termo2 = termo1
    termo1 = soma

    contador+=1

for i in (0, termos):
    somas = 0
    somas = i + somas
print(f'\n{somas} ', end='')

