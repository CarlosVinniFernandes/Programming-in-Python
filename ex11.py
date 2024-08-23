ano = int(input('Digite um ano para verificar se ele é bissexto: '))
if ano%4 == 0 and ano%100 !=0 and ano%400 !=0:
    print(f'O ano {ano} é bissexto!')

elif ano%4 == 0 and ano%100 == 0 and ano%400 ==0:
    print(f'O ano {ano} é bissexto!')

else:
    print('Nem eu sei oq aconteceu')