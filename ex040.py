nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
media = float((nota1 + nota2)/2)

if media < 5:
    print('\033[0:31mVocê está reprovado!\033[m')
elif media >= 5 and media < 6.9:
    print('\033[0:35mVocê está em recuperação!\033[m')
elif media >= 7:
    print('\033[0:32mVocê foi aprovado!\033[m')
