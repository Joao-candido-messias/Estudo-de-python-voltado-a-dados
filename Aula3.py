from random import randint

notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

nomes = []
notasJuntas = []

for i in range(len(notas_turma)):
    if i % 4 == 0:
        nomes.append(notas_turma[i])
    else:
        notasJuntas.append(notas_turma[i])


# print(nomes, notasJuntas)

# nomes.remove('Cláudia')
# print(nomes)

for i in range(0, len(notasJuntas), 3):
    notas.append([notasJuntas[i], notasJuntas[i+1], notasJuntas[i+2]])      


estudantes = nomes

def gerarId():
    return str(randint(0,99))

idEstudantes =[]

for i in range(len(estudantes)):
    idEstudantes.append((estudantes[i], estudantes[i][0] + gerarId()))


print(idEstudantes)