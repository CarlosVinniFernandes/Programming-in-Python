frase = str(input('Digite uma frase:'))
mais_repetido = frase.upper().count('A')
letra_str=0

for i in range (1,26):
    contador_de_letra = frase.upper().count(chr(65+i))

    if contador_de_letra > mais_repetido:
          mais_repetido = contador_de_letra
          letra_str = i
    print(chr(65+i), contador_de_letra, i)
print(f'A letra mais repetida foi {chr(65+letra_str),mais_repetido}')