i = 0
lista_usuario = []
while i==0:
    print(list(enumerate(lista_usuario)))

    escolha = int(input('Você quer adicionar[1], apagar[2] ou listar sua lista?'))
    if escolha == 1:
        adicao = str(input('Digite o que você quer adicionar'))
        lista_usuario.append(adicao)

    elif escolha == 2:
        indice = int(input('Digite o indice do que voce quer remover:'))

        try:
            lista_usuario.pop(indice)

        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
