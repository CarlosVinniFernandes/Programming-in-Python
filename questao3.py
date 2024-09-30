def ContadorDeNums(n, k):
    if n == 0:
        return 0
    ultimoDigito = n % 10
    if ultimoDigito == k:
        return 1 + ContadorDeNums(n // 10, k)  # -> divisão pro menor valor
    else:
        return ContadorDeNums(n // 10, k)

n = int(input("Digite um numero:"))
k = 2
quantidade = ContadorDeNums(n, k)
print("O numero ", k, " aparece ", quantidade, " vezes no número ", n)
