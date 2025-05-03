import pandas as pd     

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

dados = pd.read_csv(url, sep  =';')

dfPrecoTipo = dados.groupby('Tipo')[['Valor']].mean(numeric_only=True).sort_values('Valor')

# tiposTipo = dados.Tipo.unique()
# tiposTipo = dados.Tipo.unique()

imoveis_comerciais = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

dfImoveisResidenciais = dados.query('@imoveis_comerciais not in Tipo')

dfPrecoTipoResidenciais = dfImoveisResidenciais.groupby('Tipo')[['Valor']].mean(numeric_only=True).sort_values('Valor')

dfPrecoTipoResidenciais.to_xml('precoTipo.xml', index=True)