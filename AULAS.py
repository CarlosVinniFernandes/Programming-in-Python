def media(*args):
    if len(args) == 0:
        return 0
    soma = sum(args)  # Calcula a soma dos argumentos
    return soma / len(args)  # Divide a soma pelo número de argumentos para obter a média

soma_numero = 0
numeros = []  # Lista para armazenar os números e calcular a média mais tarde

while True:
    numero = input('Digite um número (ou algo que não seja um número para sair): ')
    if not numero.isdigit():
        break
    else:
        numero_int = int(numero)
        soma_numero += numero_int
        numeros.append(numero_int)  # Adiciona o número à lista

print("Soma total:", soma_numero)
if numeros:
    print("Média:", media(*numeros))  # Usa a função de média corretamente
else:
    print("Nenhum número foi digitado.")
