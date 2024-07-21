import random
opcoes = ["Pedra", "Papel", "Tesoura"]
pc = random.choice(opcoes)
eu = input('Você escolhe Pedra, Papel ou Tesoura?')

if pc.lower() == "pedra" and eu.lower() == "pedra" or pc.lower() == "papel" and eu.lower() == "papel" or pc.lower() == "tesoura" and eu.lower() == "tesoura":
    print('Empate')

elif eu.lower() == "pedra" and pc.lower() == "tesoura" or eu.lower() == "tesoura" and pc.lower() == "papel" or eu.lower() == "papel" and pc.lower() == "pedra":
    print('Você venceu o computador!')

else:
    print('Computador venceu :(')

print(pc)