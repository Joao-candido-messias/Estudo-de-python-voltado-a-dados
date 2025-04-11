import numpy as np
import matplotlib.pyplot as plt

dado = np.loadtxt('numpy-dados/apples_ts.csv', delimiter =',', usecols=np.arange(1,88,1))

# print(dado.ndim)      ndim:   Devolve o número de dimensões de um array.
# print(dado.size)      size:   Devolve o número de elementos de um array.
# print(dado.shape)     shape:  Devolve o número de elementos em cada dimensão do array.
# print(dado.T)         .T:     Transposição de matriz(Tranforma linhas em colunas e vice versa).

dados_transpostos = dado.T
# print(dados_transpostos)

datas = np.arange(1,88,1)
precos = dados_transpostos[:, 1:6]

# plt.plot(datas,precos[:,0]) Gera gráfico básico (x, y). O primeiro parâmetro recebido é o eixo X e o segundo o eixo Y.

# plt.show() Printa os gráficos gerados.

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

Moscow_ano_1 = Moscow[0:12]
Moscow_ano_2 = Moscow[12:24]
Moscow_ano_3 = Moscow[24:36]
Moscow_ano_4 = Moscow[36:48]
Moscow_ano_5 = Moscow[48:60]
Moscow_ano_6 = Moscow[60:72]
Moscow_ano_7 = Moscow[72:84]
Moscow_ano_8 = Moscow[84:]


# plt.plot(np.arange(1,13,1), Moscow_ano_1)
# plt.plot(np.arange(1,13,1), Moscow_ano_2)
# plt.plot(np.arange(1,13,1), Moscow_ano_3)
# plt.plot(np.arange(1,13,1), Moscow_ano_4)
# plt.plot(np.arange(1,13,1), Moscow_ano_5)
# plt.plot(np.arange(1,13,1), Moscow_ano_6)
# plt.plot(np.arange(1,13,1), Moscow_ano_7)
# plt.plot(np.arange(1,13,1), Moscow_ano_8)

# plt.legend(['Ano1', 'Ano2', 'Ano3', 'Ano4', 'Ano5', 'Ano6', 'Ano7']) # .legend: Insere legenda ao gráfico gerado.
# plt.show()

# print(np.array_equal(Moscow_ano_1, Moscow_ano_2))
# print(np.allclose(Moscow_ano_1, Moscow_ano_2,10))

Moscow_ano_a_ano = [
    Moscow_ano_1,
    Moscow_ano_2,
    Moscow_ano_3,
    Moscow_ano_4,
    Moscow_ano_5,
    Moscow_ano_6,
    Moscow_ano_7,
    # Moscow_ano_8
    ]

Moscow_ano_a_ano_array = np.array(Moscow_ano_a_ano)

# print(Moscow_ano_a_ano_array.T)


# plt.plot(datas, Kaliningrad)
# plt.show()

Kaliningrad[4]=np.mean([Kaliningrad[3], Kaliningrad[5]]);

# plt.plot(datas, Kaliningrad)
# plt.show()

print(round(np.mean(Moscow),2))
print(round(np.mean(Kaliningrad),2))


