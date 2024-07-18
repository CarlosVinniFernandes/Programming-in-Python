num = int(input('Escreva 1,2 ou 3 para converter para: Binário(1), Octa(2), Hexadecimal(3)'))
if num == 1:
    bina = int(input('Digite um número'))
    print(bin(bina)[2:])
elif num == 2 :
    octa = int(input('Digite um número'))
    print(oct(octa)[2:])
elif num == 3:
    hexa = int(input('Digie um número:'))
    print(hex(hexa)[2:])
else:
    print('Você fez besteira!')