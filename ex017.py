import math
co = float(input('Insira o valor do cateto oposto'))
ca = float(input('Insira o valor do cateto adjacente'))
#hipotenusa = co**2 + ca**2
#h = math.sqrt(hipotenusa)
h = math.hypot(co, ca)
print('Valor da hipotenusa {:.2f}'.format(h))