import pandas as pd     

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

dados = pd.read_csv(url, sep  =';')

print(dados.head(7))
print(dados.tail(5))

# print(dados)
# print(type(dados))

# print(dados['Quartos'])   Aqui vizualizamos a coluna Quartos do nosso dataframe. O parametro deve ser  o nome da nossa coluna. 
#                           Para colunas multiplas separar por virgula tal qual um array. Ex: ['Quartos', 'Vagas']

