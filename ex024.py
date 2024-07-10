cidade = str(input('Qual a sua cidade?'))
alta = cidade.upper()
comeco = alta.split()
quest = "SANTO" in comeco[0]
if (quest == False):
    {
print('Sua cidade não começa com Santo')
    }
else:
    {
print('Sua cidade começa com Santo')
    }