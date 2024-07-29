def contar_palavras(lista_de_strings):
    frequencia_palavras = {}

    for frase in lista_de_strings:
        palavras = frase.split()
        for palavra in palavras:
            if palavra in frequencia_palavras:
                frequencia_palavras[palavra] += 1
            else:
                frequencia_palavras[palavra] = 1

    return frequencia_palavras


# Teste do exercício
lista_de_strings = [
    "o rato roeu a roupa do rei de roma",
    "o rei mandou prender o rato",
    "mas o rato escapou"
]

resultado = contar_palavras(lista_de_strings)
print(resultado)
