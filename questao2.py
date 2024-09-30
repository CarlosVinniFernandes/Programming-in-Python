import math
for n in range(100):
    soma = 0
    for k in range(n + 1):
        binomial = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        soma += binomial * (2 ** k)

    if soma == 3 ** n:
        print("Caso válido em n = ", n)
    else:
        print("Caso falho para n = ", n, " soma é igual a: ", soma)
