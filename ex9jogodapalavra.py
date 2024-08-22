palavra_secreta = 'Cesupa'
palavra_tamanho = len(palavra_secreta)
print(f'A palavra tem {palavra_tamanho} letras')
palavra_fomada = ''

while True:
    resposta = input('Digite uma letra')
    for letra in palavra_secreta:

        if letra == resposta:
            palavra_fomada += letra

        else:
            palavra_fomada += '*'

    print(palavra_fomada)







