frase = """Alguns minutos de estudo 
por dia valem a pena."""
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu_at = frase.count(letra_atual)

    if letra_atual == " ":
        i += 1
        continue

    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu_at:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu_at
        letra_apareceu_mais_vezes = letra_atual

    i+=1

print('A letra que apareceu mais vezes foi '
      f'{letra_apareceu_mais_vezes}'
      f' {qtd_apareceu_mais_vezes}x')