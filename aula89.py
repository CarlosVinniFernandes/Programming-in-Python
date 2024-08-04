lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

#enumerate ->
lista_enumerada = list(enumerate(lista)) #-> "consome" os valores da lista
for item in lista_enumerada:
    print(item)

for indice, nome in lista_enumerada:
    print(indice, nome)