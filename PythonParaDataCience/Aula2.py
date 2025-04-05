notas = [5, 6, 7, 9]

def media(notas):
    resultado = round(sum(notas) / len(notas), 2)
    situacao = False
    if resultado >= 7:
        print("Aprovado")
        situacao = True
    else:
        print("Reprovado")
    return resultado, situacao

resultado, situacao = media(notas)

if situacao:
    print(resultado, "Aprovado")
else:
    print(resultado, "Reprovado")  

