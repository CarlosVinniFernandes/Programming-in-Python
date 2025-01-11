import math
def Combinatoria(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

n = 5
eq = ""

for i in range(0, n + 1):
    coef_binomial = Combinatoria(n, i)
    coeficiente = coef_binomial * (3 ** (n - i)) * ((-1) ** i)
    eq += f"{coeficiente}x^{n-i} " if n-i > 0 else f"{coeficiente} "

print(eq)
