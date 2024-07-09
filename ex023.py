#num = str(input('Digite um número de 0 a 9999\n')).zfill(4)
#print('Unidade:', num[3])
#print('Dezena:', num[2])
#print('Centena:', num[1])
#print('Milhar:', num[0])

num1 = int(input('Digite um número de 0 a 9999\n'))
div1 = num1%10
print('{}'.format(div1))
div2 = (num1%100)/10
print(int(div2))
div3 = (num1%1000)/100
print(int(div3))
div4 = (num1%10000)/1000
print(int(div4))


