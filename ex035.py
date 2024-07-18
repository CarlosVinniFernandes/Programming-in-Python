l1 = int(input('Digite um lado:'))
l2 = int(input('Digite outro lado:'))
l3 = int(input('Digite mais um lado:'))
if l1 + l2 > l3 and l3 + l1 > l2 and l3 + l2 > l1:
    print('Seu triângulo é real')
else:
    print('Seu triangulo é feike')