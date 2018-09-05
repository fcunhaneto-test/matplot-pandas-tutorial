import pandas as pl
import matplotlib.pyplot as plt

"""
Lendo um arquivo .csv com pandas e criando um pandas data frame
"""
dataframe = pl.read_csv('/home/francisco/Projects/Pycharm/'
                        'matplot-pandas-tutorial/files/annual-real-gnp-us-1909-to-1970.csv')

plt.figure(figsize=(8, 6))
plt.plot(dataframe['Year'], dataframe['GNP'])
plt.xlabel('Year')
plt.ylabel('GNP')
plt.title('PIB EUA Real Anual de 1909 a 1970')
plt.savefig('imagens/annual-real-gnp-us-1909-to-1970.png')

plt.close()

import pandas as pd
import matplotlib.pyplot as plt

"""
Lendo de um arquivo de texto
"""
with open('/home/francisco/Projects/Pycharm/matplot-pandas-tutorial/files'
          '/annual-real-gnp-us-1909-to-1970.txt', 'r') as f:
    # Usando a expressão regular para o separador indicando que eles são os
    # espaços em braco
    df = pd.read_table(f, sep='\s+')

"""
Incluindo annotates
"""
plt.figure(figsize=(8, 6))
plt.plot(dataframe['Year'], dataframe['GNP'])
plt.xlabel('Year')
plt.ylabel('GNP')
plt.title('PIB EUA Real Anual de 1909 a 1970')

# matplotlib.pyplot.annotate(*args, **kwargs)
# s:str - The text of the annotation
# xy:iterable - Length 2 sequence specifying the (x,y) point to annotate
# xytext : iterable, optional - Length 2 sequence specifying the (x,y)
#          to place the text at. If None, defaults to xy.
# arrowprops: dict, optional
plt.annotate('Fim da Segunda Gerra Mundial', xy=(1945, 355.2), color='red',
             arrowprops=dict(arrowstyle='->'), xytext=(1920, 300))
plt.annotate('Crash da Bolsa', xy=(1929, 203.6),
             arrowprops=dict(arrowstyle='->'), xytext=(1909, 200))

plt.savefig('imagens/gnp-us-1909-to-1970-annotate.png')

plt.close()

"""
Annotates dentro de um box
"""
# plt.figure(figsize=(8, 6))
# plt.plot(dataframe['Year'], dataframe['GNP'])
# plt.xlabel('Year')
# plt.ylabel('GNP')
# plt.title('PIB EUA Real Anual de 1909 a 1970')

# atributos para fonte:
# color - cor da fonte
# size - size in points or ['xx-small', 'x-small', 'small', 'medium', 'large',
#          'x-large', 'xx-large']
# weight - ['light' | 'ultralight' | 'normal' | 'bold' | 'heavy' | 'ultrabold'
# style - ['normal' | 'italic' | 'oblique']
# family - ['serif' | 'sans-serif' | 'cursive' | 'fantasy' | 'monospace']
# plt.annotate(
#     'Fim da Segunda Gerra Mundial',
#     xy=(1945, 355.2),
#     color='red',
#     size='14',
#     arrowprops=dict(arrowstyle='->'), xytext=(1920, 500),
#     bbox = dict(boxstyle='round,pad=0.2', fc='yellow',
#                 alpha=0.3),
# )
# plt.annotate(
#     'Crash da Bolsa', xy=(1929, 203.6),
#     arrowprops=dict(arrowstyle='->'),
#     xytext=(1909, 200),
#     color='yellow',
#     weight='heavy',
#     style='italic',
#     bbox = dict(boxstyle='round,pad=0.2', fc='red',
#                 alpha=1),
# )
#
# plt.savefig('gnp-us-1909-to-1970-annotate-box.png')
#
# plt.close()

"""
Incluindo texto no gráfico
"""
font_1 = {'family':'serif', 'color':'#FFFC19', 'fontsize':'large' }
font_2 = {'family':'fantasy', 'color':'yellow', 'size':'16'}
font_3 = {'family':'serif', 'color':'yellow', 'size':'18', 'weight':'bold'}

plt.figure(figsize=(8, 6))
plt.plot(dataframe['Year'], dataframe['GNP'])
plt.xlabel('Year')
plt.ylabel('GNP')
plt.title('Annual Real USA GNP 1909 to 1970')

plt.annotate('Fim da Segunda Gerra Mundial', xy=(1945, 355.2),
             arrowprops=dict(arrowstyle='->'), xytext=(1920, 300))
plt.annotate('Crash da Bolsa', xy=(1929, 203.6),
             arrowprops=dict(arrowstyle='->'), xytext=(1909, 200))

# class matplotlib.text.Annotation(s, xy, xytext=None, xycoords='data',
# textcoords=None, arrowprops=None, annotation_clip=None, **kwargs)
plt.text(1909, 500, 'Pequeno texto de exemplo 1', fontdict=font_1,
         backgroundcolor='#0971B2')

plt.text(1909, 600, 'Pequeno texto de exemplo 2', fontdict=font_2,
         backgroundcolor='#000000')

# horizontalalignment or ha 	[ 'center' | 'right' | 'left' ]
# verticalalignment or va 	[ 'center' | 'top' | 'bottom' | 'baseline' ]
plt.text(1940, 700, 'Pequeno texto de exemplo 3', fontdict=font_3,
         backgroundcolor='#000000', horizontalalignment='center',
         verticalalignment='top')

plt.savefig('imagens/gnp-us-1909-to-1970-text.png')

plt.close()
