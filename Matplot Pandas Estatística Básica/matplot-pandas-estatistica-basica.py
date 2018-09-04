import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandasUteis.pandas_utils import frequency_by_natural_order

"""
Criando um histograma para os totais de cada idade
"""
df = pd.read_csv('/home/francisco/Projects/Pycharm/'
                        'matplot-pandas-tutorial/files/questionario.csv')

pd.set_option('precision', 2)
pd.options.display.float_format = '{:,.2f}'.format

idades_group = frequency_by_natural_order(df, 'Idade')

with open('idade-groups.txt', 'w') as f:
    idades_group.to_string(f)

x = idades_group.index
y = np.array(idades_group['freq']) * 100

plt.figure(figsize=(8, 6))
plt.title('Distribuição de Idades')
plt.xlabel('Idade')
plt.ylabel('Frequencia %')
plt.xticks(x) # obriga a mostrar todos os números no eixo x
plt.bar(x, y)
plt.savefig('ditribuicao-idades.png')
plt.close()

"""
Agrupando os valores dos pesos e extraindo os totais e as frequencias
"""