string = 'ABCD'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria', 'Helena',],
    ['Elaine',],
    ['Luiz', 'João', 'Eduarda',],
]

# a,b,c, *_ = lista
# print(a,c)
#
# a,b,*_,ap,u = lista
# print(a,ap,u)
for nome in lista:
    print(nome, end=' ', sep='')

print(*lista)
print(*tupla)
print(*salas, sep='\n')