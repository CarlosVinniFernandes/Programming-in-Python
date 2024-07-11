nome = str(input('Qual o seu nome completo?\n'))
div = nome.split()
primeiro = div[0]
print('Primeiro:', primeiro)
ultimo = nome.rsplit()
print('Ultimo:', ultimo[-1])