# High Order Functions -> Funções que podem receber e/ou retornar
#outras funções
def saudacao(msg):
    return msg

def executa(funcao, msg):
    return funcao(msg)

v = executa(saudacao, 'Bom dia')
print(v)

def saudacao2(msg, nome):
    return f'{msg}, {nome}'

def executa2(funcao, *args):
    return funcao(*args)

print(executa2(saudacao2, 'Bom dia','Acorde'))
