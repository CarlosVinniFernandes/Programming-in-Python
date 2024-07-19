ano = int(input('Em que ano você nasceu?'))
alist = 2024 - ano

if alist >= 18:
    print('Você está na idade para se alistar!')
if alist > 18:
    prazo = alist - 18
    print('Você tem {} anos e passou {} anos do prazo!'.format(alist, prazo))
elif alist <= 18:
    prazo2 = 18 - alist
    print('Você ainda não precisa se alistar e falta {} anos para seu alistamento'.format(prazo2))