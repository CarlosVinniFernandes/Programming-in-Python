nome = str(input('Qual o seu nome completo?')).strip()
alta = nome.upper()
buscador = alta.find('SILVA')
if (buscador == -1):
    {
    print('Seu nome não tem Silva!')
    }
else:{
    print('Seu nome tem Silva!')
}