num = float(input('Qual a distância que você irá percorrer?'))
if num <= 200:
    soma = num * 0.5
    print('Por viajar {}Km, você pagará {}'.format(num, soma))
else:
    soma2 = num * 0.45
    print('Por viajar {}Km, você pagará {}'.format(num, soma2))