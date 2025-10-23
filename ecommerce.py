import pandas as pd 
import matplotlib.pyplot as plt

#ver todas as colunas e tipos de dados 
df  = pd.read_csv("olist_customers_dataset.csv")
print(df.info())

#aqui vemos o numero de linhas e colunas 
print(df.shape)

linhas, colunas = df.shape
print(f"o Dataset tem {linhas} linhas e {colunas } colunas.")

colunas = df.columns
print(f"o Dataset tem as seguintes colunas :{colunas}.")

#quantos clientes tem em cada estado?
clientes_por_estado = df['customer_state']. value_counts()

print(clientes_por_estado.head(10))

#Quais cidades têm maior concentração de clientes?

clientes_por_cidade =df['customer_city']
print(clientes_por_cidade)

#Mapemento de regiões 

regioes = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste',
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'}

#Criar coluna de região
df['customer_region'] = df['customer_state'].map(regioes)

clientes_por_região = df['customer_region'].value_counts(normalize=True)*100
print(f"clientes por regiao :{clientes_por_região.round(2)}")

#Visualização dos Dados

clientes_por_estado = df['customer_state']. value_counts().head(10)
plt.figure(figsize=(10,5))
clientes_por_estado.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Estados com Mais Clientes')
plt.xlabel('Estado')
plt.ylabel('Quantidade de clientes')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle = '--', alpha=0.7)
plt.show()


clientes_por_cidade =df['customer_city'].value_counts().head(10)
plt.figure(figsize=(12,5))
clientes_por_cidade.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('top 10 cidades com mais clientes')
plt.xlabel('cidade')
plt.ylabel('Quantidade de clientes')
plt.grid(axis='y',linestyle = "--", alpha=0.7)
plt.show()


regioes = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste',
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'}

df['customer_region'] = df['customer_state'].map(regioes)
clientes_por_região = df['customer_region'].value_counts()

#Gráfico de pizza

plt.figure(figsize=(7, 7))
clientes_por_região .plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99','#ffcc99','#ff9999','#c2c2f0'])
plt.title('Distribuição de Clientes por Região do Brasil')
plt.ylabel('')
plt.show()