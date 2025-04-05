
notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

estudante = input("Insira o nome do estudante:")

try:
   resultado = notas[estudante]
except KeyError as e:
    print(type(e), f"Erro: {e} - Estudante não matriculado.")
else:
    print("Estas são as notas de {}:".format(estudante),resultado)
finally:
    print("Consulta encerrada.")