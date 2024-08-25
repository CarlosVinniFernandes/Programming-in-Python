def multiplicador(x,y,*args):
    mult = x * y
    for numeros in args:
        mult *= numeros
    return mult

valor = multiplicador(2, 5, 10, 10, 10, 5,20)
def impar(valor):
    if valor%2==0:
        return f'{valor} é par'
    else:
        return f'{valor} é impar'
print(valor)
print(impar(valor))


