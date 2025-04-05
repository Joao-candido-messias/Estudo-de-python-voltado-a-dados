notas = [[8.0, 9.0, 10.0],[ 9.0, 7.0, 6.0],[3.4, 7.0, 7.0] ,[5.5, 6.6, 8.0] ,[6.0, 10.0, 9.5] ]
nomes = ['João', 'Maria', 'José', 'Cláudia', 'Ana']
def calcularMedia(lista: list[0]) -> float:
    media = round(sum(lista)/len(lista), 2)
    return media
    
medias = []

for i in notas:
    medias.append(calcularMedia(i))

print(medias)

mediasParaPrintar = []

for i in range(len(medias)):
    mediasParaPrintar.append((nomes[i],medias[i]))

print(mediasParaPrintar)

