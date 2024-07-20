altura = float(input('Qual sua altura?'))
peso = float(input('Qual seu peso?'))
imc = peso/altura**2
print('Seu peso é {:.2f}\n e '.format(imc))
if imc < 18.5:
    print('Você está na categoria Abaixo do Peso!')
elif imc > 18.5 and imc < 25:
    print('Você está na categoria Peso Ideal!')
elif imc > 25 and imc < 30:
    print('Você está na categoria Obesidade!')
elif imc > 30 and imc < 40:
    print('Você está na categoria Obesidade Mórbida!')
else:
    print('Digite corretamente!')

