casa = int(input('Quantos reais é a casa?'))
salario = int(input('Quanto é seu salário?'))
anos = int(input('Quantos anos você vai querer parcelar?'))

ano = anos*12
parcela = casa/ano
trinta = parcela*30/100
permitido = parcela - trinta
if parcela > trinta:
    print('\033[0;31;40mA parcela ficará {:.2f}R$ acima do permitido, logo seu empréstimo foi negado.\033[m'.format(permitido))