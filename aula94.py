# Lista de de listas e seus indices

salas = [

    ['Maria', 'Helena',],

    ['Elaine',],

    ['Luiz', 'João', 'Eduarda',(0,10,20,30,40)],
]

# print(salas[2])
# print(salas[2][3])
# print(salas[2][3][3])
for sala in salas:
    for aluno in sala:
        print(aluno)
