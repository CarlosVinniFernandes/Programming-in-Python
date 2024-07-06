k = float(input('Quantos km você rodou?'))
d = float(input('Quantos dias você usou o carro?'))
sk = 0.15 * k
sd = 60 * d
st = sk + sd
print('Você rodou {}km e lhe custou {}RS'.format(k, sk))
print('e usou por {}dias, custando-lhe {}RS'.format(d, sd))
print('Totalizando {}'.format(st))