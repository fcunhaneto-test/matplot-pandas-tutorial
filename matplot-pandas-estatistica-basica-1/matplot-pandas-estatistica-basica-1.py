import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandasUteis.pandas_utils import frequency_by_buckets

df = pd.read_csv('/home/francisco/Projects/Pycharm/'
                        'matplot-pandas-tutorial/files/questionario.csv')

"""
Criando um histograma para com os pesos dos alunos
"""
peso = df['Peso']

plt.figure(figsize=(8, 6))
plt.hist(peso, bins=range(40, 110,10))
plt.title('Distribuição de Pesos')
plt.xlabel('Peso')
plt.ylabel('Alunos')
plt.savefig('imagens/peso-histograma.png')
plt.close()

"""
Criando um histograma comparando os pesos masculino x feminino
"""
fem = df[df.Sexo == 'F']
mas = df[df.Sexo == 'M']
peso_fem = fem['Peso']
peso_mas = mas['Peso']

plt.figure(figsize=(8, 6))

"""
sobre a função hist(x, bins=None, color=None, label=None, **kwargs)

x: Valores de entrada, um array único ou uma sequência de arrays

bins: Inteiro ou sequência ou 'auto', opcional

labels: String ou sequência de strings para corresponder a vários conjuntos de dados

color: Especificação de cores ou sequência de especificações de cores

Mais em:
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
"""
plt.hist(peso_fem, bins=range(40, 110,10),
         label='feminino', color='#FF26E1', alpha=0.5)
plt.hist(peso_mas, bins=range(40, 110,10),
         label='masculino', color='#2DB200', alpha=0.5)

plt.title('Distribuição de Pesos')
plt.xlabel('Peso')
plt.ylabel('Alunos')
plt.legend(loc='upper right')
plt.savefig('imagens/peso-histograma-mas-x-fem.png')
plt.close()

"""
Criando um diagrama de barras para os totais de cada idade
"""
idade = df['Idade']
idade_sum = idade.value_counts()
idade_sum = idade_sum.sort_index()

x = idade_sum.index
y = idade_sum

plt.figure(figsize=(8, 6))

"""
sobre a função bar(*args, **kwargs)
Parameters:

x:  As coordenadas x das barras
y:  A altura (s) das barras

Mais em:
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html
"""
plt.bar(x, y)

plt.title('Distribuição de Idades')
plt.xlabel('Idade')
plt.ylabel('Alunos')
plt.xticks(x) # obriga a mostrar todos os números no eixo x
plt.savefig('imagens/idades-diagrama-barras.png')
plt.close()

"""
Criando um diagrama de barras da distribuição de pesos separados entre feminino
e masculino
"""
fem = df[df.Sexo == 'F']
mas = df[df.Sexo == 'M']

peso_fem = frequency_by_buckets(fem, 'Peso', 10, 40, 100)
peso_mas = frequency_by_buckets(mas, 'Peso', 10, 40, 100)

peso = np.arange(40, 100, 10)

df_mas_fem = pd.DataFrame({
    'peso': peso,
    'fem': peso_fem['Peso'],
    'mas': peso_mas['Peso']
})

fig = plt.figure(figsize=(8, 7)) # Create matplotlib figure

ax = fig.add_subplot(111) # Create matplotlib axes

width = 0.5 # espaço entre as barras feminina masculina no eixo x

plt.title('Distribuição de Pesos Feminino e Masculino')
plt.xlabel('Peso')
plt.ylabel('Alunos')

df_mas_fem.fem.plot(kind='bar', color='#FF26E1', ax=ax, width=width, position=0,
                    alpha=0.5, label='feminino')
df_mas_fem.mas.plot(kind='bar', color='#2DB200', ax=ax, width=width, position=1,
                    alpha=0.5, label='masculino')
plt.legend(loc='upper right')
plt.savefig('imagens/peso-diagrama-barras-mas-x-fem.png')
plt.close()
