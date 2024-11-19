def inverso_modular(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def teorema_chines_restos(a, m):
    M = 1
    for mod in m:
        M *= mod

    resultado = 0
    for i in range(len(a)):
        Mi = M // m[i] 
        inverso = inverso_modular(Mi, m[i]) 
        resultado += a[i] * Mi * inverso 

    return resultado % M 
    
#um exemplo de como seria usado:

a = [2, 3, 1]  # Coloca aqui os a (numero da esquerda do mod)
m = [3, 5, 7]  # Módulos (mod)

solucao = teorema_chines_restos(a, m)
print(f"x = {solucao}")
