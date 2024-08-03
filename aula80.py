# listas em python
# tipo list - mutável
# suporta varios valores de qualquer tipo
# conhecimentos reutilizaveis - indices e fatiamento
# metodos uteis: append, insert, pop, del, clear, extend,+
#lista vazia é falsa
# string = 'ABCDE'
# lista = [123, True, 'Luiz Otávio',1.2,[]]
# print(lista[2])
# append -> adiciona no final da lista
# pop -> remove o final da lista
# del -> apaga um indice
# clear -> limpa a lista
#extend -> estende a lista
lista = [10,20,30,40]
lista[2] = 300
del lista[2]
ultimo_valor = lista.pop()
print(lista)
print(lista, ultimo_valor)
print(lista, lista.insert(1,777))