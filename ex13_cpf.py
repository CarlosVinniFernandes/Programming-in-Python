import random
cpf = ''
for l in range(0,9):
    cpf += str(random.randint(0,11))

print(cpf)
cpf = ''.join([c for c in cpf if c.isdigit()]) # replace('-', '')
nove_digitos = cpf[0:9]
digitos = (int(d) for d in nove_digitos)
soma = 0; soma_2 = 0
multiplicador = 11
teste = 'len'

for i in range(10,1,-1):
    for numeros in digitos:
        soma += numeros*i
        break

divisao_soma = (soma*10)%11
verificador = 0 if divisao_soma > 9 else divisao_soma

dez_digitos = nove_digitos+str(verificador)
for numbers in dez_digitos:
    soma_2 += int(numbers)*multiplicador
    multiplicador -= 1

divisao_soma_2 = (soma_2*10)%11
verificador_2 = 0 if divisao_soma_2 > 9 else divisao_soma_2
onze_digitos = dez_digitos+str(verificador_2)

print(verificador, verificador_2)