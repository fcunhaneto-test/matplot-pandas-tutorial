import numpy as np
import pandas as pl
import matplotlib.pyplot as plt

"""
Plotagem de uma reta simples f(x) = 2x
"""
# arr1 = np.array([1, 2, 3, 4, 5, 6, 7 ,8, 9, 10])
# arr2 = np.array([2, 4, 6, 8, 10, 12, 14 ,16, 18, 20])
#
# plt.figure(figsize=(6, 4))
# plt.plot(arr1, arr2)
# plt.savefig('reta-simples.png')

"""
Acrescentando Grid
"""
# arr1 = np.array([1, 2, 3, 4, 5, 6, 7 ,8, 9, 10])
# arr2 = np.array([2, 4, 6, 8, 10, 12, 14 ,16, 18, 20])
#
# plt.figure(figsize=(6, 4))
# plt.plot(arr1, arr2)
# plt.xlabel('x')
# plt.ylabel('f(x) = x + 3')
# plt.grid(True)
# plt.savefig('reta-simples-labels.png')

"""
Acrescentando Grid
"""
# arr1 = np.array([1, 2, 3, 4, 5, 6, 7 ,8, 9, 10])
# arr2 = np.array([2, 4, 6, 8, 10, 12, 14 ,16, 18, 20])
#
# plt.figure(figsize=(6, 4))
# plt.plot(arr1, arr2)
# plt.xlabel('x')
# plt.ylabel('f(x) = 2x')
# plt.grid(True)
# plt.savefig('reta-simples-grid.png')

"""
Mais de uma linha no gráfico
"""
# x = np.arange(1, 11)
# print(x)
#
# plt.figure(figsize=(6, 4))
# plt.plot(x, 2*x)
# plt.plot(2*x, x/2)
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.grid(True)
# plt.savefig('reta-simples-duas.png')

"""
Escolhendo cores para as retas
"""
x = np.arange(1, 11)
print(x)

plt.figure(figsize=(6, 4))
plt.plot(x, 2*x, color='#17a589') # green
plt.plot(2*x, x/2, color='red')
plt.plot(x, x+3, color='#f4d03f') # yellow
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.savefig('reta-simples-cores.png')
