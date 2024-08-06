# x = 5
# print(f'A soma de {x = }')
def soma(x,y):
    #definicao
    print(x+y)
x = int(input('coloca ai'))
y = int(input('coloca ai mano'))
print(soma(x,y))

def soma2(x,y,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} =', x + y + z)
    else:
        print(f'{x=} {y=} =', x + y)

soma2(2,3)

