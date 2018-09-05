import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/francisco/Projects/Pycharm/matplot-pandas-tutorial/'
                 'files/questionario.csv')

"""
Criando um boxplot para a coluna alturas
"""

alturas = df['Alt']
alt_descri = alturas.describe()

with open('altura-descricao.txt', 'w') as f:
    alt_descri.to_string(f)

q1 = alt_descri['25%']
mediana = alt_descri['50%']
q2 = alt_descri['75%']

s_q1 = "{0:.2f}".format(q1)
s_mediana = "{0:.2f}".format(mediana)
s_q2 = "{0:.2f}".format(q2)

font_1 = {'family': 'serif', 'color': 'darkred', 'size':'14'}

plt.figure(figsize=(6, 7))
plt.boxplot(alturas)
plt.title('Boxplot Alturas')
plt.ylabel('Altura')
plt.text(1, q1, s_q1, fontdict=font_1)
plt.text(1, mediana, s_mediana, fontdict=font_1)
plt.text(1, q2, s_q2, fontdict=font_1)
plt.savefig('imagens/alturas-boxplot.png')
plt.close()

"""
Criando um boxplot para a coluna alturas, e para as alturas femininas e 
masculinas
"""
alt = df['Alt']
alt_f = df[df.Sexo == 'F']
alt_f = alt_f['Alt']
alt_m = df[df.Sexo == 'M']
alt_m = alt_m['Alt']

alt_d = alt.describe()
alt_fd = alt_f.describe()
alt_md = alt_m.describe()

s_describe = {'G': alt_d, 'F': alt_fd, 'M': alt_md}

for x in s_describe:
    f_name = 'altura-descricao-{0}.txt'.format(x)
    with open(f_name, 'w') as f:
        alt_descri.to_string(f)


font_1 = {'family':'serif', 'color':'#993556'}
font_2 = {'family':'serif', 'color':'#5C1BCC'}
font_3 = {'family':'serif', 'color':'000', 'size':12}
font_4 = {'family':'serif', 'color':'#CC904A'}

fig = plt.figure(figsize=(6, 8))
plt.boxplot([alt, alt_f, alt_m], labels=['Geral', 'Fem', 'Masc'])

plt.title('Boxplot Alturas Geral, Feminina e Masculina')
plt.xticks([1, 2, 3], ['G', 'F', 'M'])
plt.ylabel('Idade')

i = 1
for ax in s_describe:

    plt.text(i, s_describe[ax]['50%'], '{0:.2f}'.format(s_describe[ax]['50%']),
                           fontdict=font_2)
    plt.text(i, s_describe[ax]['25%'], '{0:.2f}'.format(s_describe[ax]['25%']),
             fontdict=font_1)
    plt.text(i, s_describe[ax]['75%'], '{0:.2f}'.format(s_describe[ax]['75%']),
             fontdict=font_1)
    i += 1

plt.text(2.1, alt_fd['min'], '{0:.2f}'.format(alt_fd['min']),
             fontdict=font_4)
plt.text(2.1, alt_fd['max'], '{0:.2f}'.format(alt_fd['max']),
             fontdict=font_4)

plt.text(2.8, 1.45, 'G - Geral\nF - Feminino\nM - Masculino',
         horizontalalignment='left', fontdict=font_1)
plt.savefig('imagens/alturas-geral-fem-masc-boxplot.png')
plt.close()

"""
Criando um Diagrama de Pizza para a coluna OpTV(Opnião sobre a programação de TV)
"""
optv = df['OpTV']
optv_sum = optv.value_counts()

total = df['OpTV'].count()
optv_freq = (optv_sum / total) * 100

plt.figure(figsize=(6,6))
labels = ['Ruim', 'Média', 'Boa', 'Não Sabe']
colors = ['#A43820', '#FFF8C6', '#99C68E', '#4DBCD3']
explode = (.1, 0, .1, 0) # Separa uma das fatias de acordo com indice e o
# valor dado(.1)

"""
Sobre o gráfico de pizza:

x: The wedge sizes.

autopct: Se não for Nenhum, é uma string ou função usado para rotular as
 cunhas com seu valor numérico.

colors: Uma sequência de args de matplotlib por meio da qual o gráfico de
 pizza será alternado.

explode: Se não for None, é uma matriz len(x) que especifica a fração do raio
 com a qual deslocar cada cunha.

shadow: Se True desenhe uma sombra sob o gráfico.

Mais em: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html
"""
plt.pie(optv_freq, labels=labels ,  autopct='%1.1f%%', colors=colors,
        shadow=True, explode=explode)
plt.savefig('imagens/opniao-tv-diagrama-pizza.png')
plt.close()
