condicao = True
while condicao == True:
    n1 = float(input('Digite um numero:'))
    n2 = float(input('Digite um numero:'))
    operador = str(input('''
Digite um operador: [+]
Digite um operador: [-]
Digite um operador: [*]
Digite um operador: [/]
Digite um operador: [//]
Digite um operador: [%]
Digite um operador: [**]\n'''))

    if operador == '+':
        op = n1 + n2
        print(f'Seu valor de {n1}+{n2} = {op}')
        decisao = str(input('Deseja continuar?[S]im ou [N]ão: '))
        if decisao.lower().startswith('s') == True:
            condicao = True
        else:
            condicao = False

    elif operador == '-':
        op = n1 - n2
        print(f'Seu valor de {n1}-{n2} = {op}')
        decisao = str(input('Deseja continuar?[S]im ou [N]ão: '))
        if decisao.upper() == 'S':
            condicao = True
        else:
            condicao = False

    elif operador == '*':
        op = n1 * n2
        print(f'Seu valor de {n1}*{n2} = {op}')
        decisao = str(input('Deseja continuar?[S]im ou [N]ão: '))
        if decisao.upper() == 'S':
            condicao = True
        else:
            condicao = False

    elif operador == '**':
        op = n1 ** n2
        print(f'Seu valor de {n1}**{n2} = {op}')
        decisao = str(input('Deseja continuar?[S]im ou [N]ão: '))
        if decisao.upper() == 'S':
            condicao = True
        else:
            condicao = False

    elif operador == '/':
        op = n1 / n2
        print(f'Seu valor de {n1}/{n2} = {op}')
        decisao = str(input('Deseja continuar?[S]im ou [N]ão: '))
        if decisao.upper() == 'S':
            condicao = True
        else:
            condicao = False

    elif operador == '//':
        op = n1 // n2
        print(f'Seu valor de {n1}//{n2} = {op}')
        decisao = str(input('Deseja continuar?[S]im ou [N]ão: '))
        if decisao.upper() == 'S':
            condicao = True
        else:
            condicao = False

    elif operador == '%':
        op = n1 % n2
        print(f'Seu valor de {n1}%{n2} = {op}')
        decisao = str(input('Deseja continuar?[S]im ou [N]ão: '))
        if decisao.upper() == 'S':
            condicao = True
        else:
            condicao = False
print('Obrigado por usar a calculadora :)')

