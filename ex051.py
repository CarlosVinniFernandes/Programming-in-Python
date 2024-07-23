primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for i in range(10):
    termo_atual = primeiro_termo + i * razao
    print(termo_atual)
