import numpy as np 

dado = np.loadtxt('numpy-dados/apples_ts.csv', delimiter =',', usecols=np.arange(1,88,1))

# print(dado.ndim)      ndim:   Devolve o número de dimensões de um array
# print(dado.size)      size:   Devolve o número de elementos de um array
# print(dado.shape)     shape:  Devolve o número de elementos em cada dimensão do array
# print(dado.T)         .T:     Transposição de matriz(Tranforma linhas em colunas e vice versa)

dados_transpostos = dado.T
print(dados_transpostos)

