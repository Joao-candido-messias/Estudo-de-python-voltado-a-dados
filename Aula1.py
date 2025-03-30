import matplotlib.pyplot as plt
from random import choice

estudantes = ["João", "Maria", "Pedro", "Ana"]

notas = [8.5, 9.0, 7.0, 8.0]
plt.bar(estudante, notas)
plt.show()

escolhido = choice(estudantes)
print(escolhido)


