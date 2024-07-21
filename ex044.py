produto = 1246
decisao = input("Qual vai ser a forma de pagamento? Cartão[C] ou À vista[A]? ")

if decisao.lower() == "c":
        parcela = input('De quantas vezes você vai pagar? 1x, 2x ou 3x?')
        if parcela == "1":
            preco = produto*0.95
            print('Seu produto de {:.2f}R$, ficará {:.2f}R$ à vista no cartão'.format(produto, preco))
        elif parcela == "2":
            div = produto/2
            print('Seu produto de {:.2f}R$, ficará {:.2f}R$ de 2x sem juros'.format(produto, div))
        elif parcela == "3":
            preco3 = produto*1.20
            print('Seu produto de {:.2f}R$, ficará {:.2f}R$ de 3x com 20% de juros'.format(produto, preco3))
        else:
            print('Voce fez besteira')

elif decisao.lower() == "a":
        vista = produto*.90
        print(f'Seu produto de {produto:.2f}R$, ficará {vista:.2f}R$ à vista no dinheiro!')

else:
        print('Voce fez besteira')