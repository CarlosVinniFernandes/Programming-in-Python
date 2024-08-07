# def criar_saudacao(saudacao, nome):
#     def saudar():
#        return f'{saudacao}, {nome}!'
#     return saudar
#
# s1 = criar_saudacao('Bom dia', 'Luiz')
# s2 = criar_saudacao('Boa noite', 'Luiz')
# print(s1)
# print(s2())

def criar_saudacao(saudacao):
    def saudar(nome):
       return f'{saudacao}, {nome}!'
    return saudar


falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joao', 'Luiz']:
    print(falar_bomdia(nome))
    print()
    print(falar_boanoite(nome))
