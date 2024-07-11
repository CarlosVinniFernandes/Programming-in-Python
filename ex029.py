carro = int(input('Em que velocidade você estava?\n'))
if carro > 80:
    print('Você foi multado!')
if carro > 80:
    soma = carro - 80
    multa = soma * 7
    print('Você pagará {} de multa, pois ultrapasou {} Km do permitido'.format(multa, soma))
else:
    print('Você está na lei!')