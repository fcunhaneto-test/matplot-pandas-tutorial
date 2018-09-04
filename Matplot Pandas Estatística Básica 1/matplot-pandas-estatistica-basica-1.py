import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandasUteis.pandas_utils import frequency_by_natural_order, frequency_by_buckets

"""
Criando um histograma para os totais de cada idade usando a função hist() do 
Matplot
"""
df = pd.read_csv('/home/francisco/Projects/Pycharm/'
                        'matplot-pandas-tutorial/files/questionario.csv')

idade = df['Idade']

plt.figure(figsize=(8, 6))
plt.title('Distribuição de Idades')
plt.xlabel('Idade')
plt.ylabel('Alunos')
plt.hist(idade, bins=[17, 18, 19, 20, 21, 22, 23, 25, 25],
         alpha=0.5, label='Idade')
plt.legend(loc='upper right')
plt.savefig('idade-histograma.png')
plt.close()

"""
Criando um histograma comparando os pesos masculino x feminino
"""
fem = df[df.Sexo == 'F']
mas = df[df.Sexo == 'M']
peso_fem = fem['Peso']
peso_mas = mas['Peso']

plt.figure(figsize=(8, 6))
plt.title('Distribuição de Pesos')
plt.xlabel('Peso')
plt.ylabel('Alunos')
plt.hist(peso_fem, bins=[40, 50, 60, 70, 80, 90, 100],
         alpha=0.5, label='feminino', color='#FF26E1')
plt.hist(peso_mas, bins=[40, 50, 60, 70, 80, 90, 100],
         alpha=0.5, label='masculino', color='#2DB200')
plt.legend(loc='upper right')
plt.savefig('peso-mas-x-fem.png')
plt.close()

"""
Criando um diagrama de barras para os totais de cada idade
"""
pd.set_option('precision', 2)
pd.options.display.float_format = '{:,.2f}'.format

idades_group = frequency_by_natural_order(df, 'Idade')

with open('idade-ditribuicao.txt', 'w') as f:
    idades_group.to_string(f)

x = idades_group.index
y = np.array(idades_group['freq']) * 100

plt.figure(figsize=(8, 6))
plt.title('Distribuição de Idades')
plt.xlabel('Idade')
plt.ylabel('Frequencia %')
plt.xticks(x) # obriga a mostrar todos os números no eixo x
plt.bar(x, y)
plt.savefig('idades-ditribuicao.png')
plt.close()

"""
Agrupando os valores dos pesos e extraindo os totais e as frequencias e
criando um histograma
"""

peso_group = frequency_by_buckets(df, 'Peso', 10, 40, 100)

with open('peso-groups.txt', 'w') as f:
    idades_group.to_string(f)

y = peso_group['freq'] * 100
x = []
for p in peso_group.index:
    x.append(str(p))

plt.figure(figsize=(8, 6))
plt.bar(x, y)
plt.title('Distribuição de Pesos')
plt.xlabel('Peso')
plt.ylabel('Frequencia')
plt.savefig('peso-ditribuicao.png')
plt.close()

"""
Agrupando os valores dos pesos para homens e mulheres e criando um diagrama 
de barras
"""
fem = df[df.Sexo == 'F']
mas = df[df.Sexo == 'M']

peso_fem = frequency_by_buckets(fem, 'Peso', 10, 40, 100)
peso_mas = frequency_by_buckets(mas, 'Peso', 10, 40, 100)

peso = [x for x in range(40, 100, 10)]

df_mas_fem = pd.DataFrame({
    'peso': peso,
    'fem': peso_fem['Peso'],
    'mas': peso_mas['Peso']
})

fig = plt.figure(figsize=(8, 7)) # Create matplotlib figure

ax = fig.add_subplot(111) # Create matplotlib axes

width = 0.5

plt.title('Distribuição de Pesos')
plt.xlabel('Peso')
plt.ylabel('Alunos')

df_mas_fem.fem.plot(kind='bar', color='#FF26E1', ax=ax, width=width, position=0,
                    alpha=0.5, label='feminino')
df_mas_fem.mas.plot(kind='bar', color='#2DB200', ax=ax, width=width, position=1,
                    alpha=0.5, label='masculino')
plt.legend(loc='upper right')
plt.savefig('peso-ditribuicao-mas-x-fem.png')
