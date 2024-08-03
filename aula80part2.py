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
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
#lista_d = lista_a.extend(lista_b) #--> muda a operação diretamente na lista
# print(lista_c)
# print(lista_d)
# print(lista_a)
print(lista_a.insert(1 , 5))