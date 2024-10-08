# """
# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - Força o número a aparecer antes dos zeros
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a
# """
vari = 'ABC'
print(f'{vari}')
print(f'{vari:>10}')
print(f'{vari:<10}.')
print(f'{vari:^10}')
print(f'{vari:>10}')
print(f'{1000.123124128390218321321:-,.1f}')#- só vai aparecer se o numero for neg
print(f'{vari:>10}')