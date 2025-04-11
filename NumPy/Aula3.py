import numpy as np
import matplotlib.pyplot as plt

dado = np.loadtxt('numpy-dados/apples_ts.csv', delimiter =',', usecols=np.arange(1,88,1))

dados_transpostos = dado.T

datas = np.arange(1,88,1)
precos = dados_transpostos[:, 1:6]

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

Kaliningrad[4]=np.mean([Kaliningrad[3], Kaliningrad[5]]);

print(round(np.mean(Moscow),2))
print(round(np.mean(Kaliningrad),2))

plt.plot(datas, Moscow)
plt.show()



