n1 = float(input('Digite o primeiro número'))
n2 = float(input('Digite o segundo número'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a divisão é {:.3f}'.format(s, m, d), end='')
print('A divisão inteira {} e a potencia {}'.format(di,e))
#\n quebra a frase e o end='' deixa unido.