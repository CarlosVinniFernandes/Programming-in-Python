l1 = int(input('Digite um lado:'))
l2 = int(input('Digite outro lado:'))
l3 = int(input('Digite mais um lado:'))
if (l1 + l2 > l3 and l3 + l1 > l2 and l3 + l2 > l1):

    print('Seu triângulo é real')
    if (l1 == l2 and l1 == l3):

        print('Seu triângulo é também equilátero')

    elif (l1 == l2 and l2 != l3 or l1 != l2 and l2 == l3 or l1 != l2 and l1 == l3):
        print('Seu triângulo é também isósceles')

    elif (l1 != l2 or l2 != l3 or l1 != l3):
        print('Seu triângulo é também escaleno')


else:
    print('Seu triangulo é feike')