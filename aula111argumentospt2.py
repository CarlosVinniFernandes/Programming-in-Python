x, y, *resto = 1, 2, 3, 4
print(x,y,resto)

def soma(*args):
    #args = list(args)
    #print(args)
    total = 0
    for numero in args:
        total += numero
    return total

soma1_2_3 = soma(1,2,3,4,5,6)
print(soma1_2_3)

soma1_2_3 = (1,2,3,4,5,6)
print(sum(soma1_2_3))

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
print(numeros)
print(*numeros)
