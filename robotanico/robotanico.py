#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy  as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv('iris.csv')

# print(df.head())

#AS COLUNAS DOS DADOS
# print(df.columns)


# DESCRIÇÃO DOS DADOS

# pr1int(df.describe())

X = np.array(df.drop('target', 1))
Y = np.array(df.target)
# print(X)
# print(Y)
#PLOTANDO A DISPERÇÃO DOS DADOS
sb.pairplot(df, hue='target')


#INTERAÇÃO:
dados_flor = []
altura_sepala = input("Digite a altura da sepala:")
dados_flor.append(float(altura_sepala))
largura_sepala = input("Digite a largura da sepala:")
dados_flor.append(float(largura_sepala))

altura_petala = input("Digite a altura da petala:")
dados_flor.append(float(altura_petala))
largura_petala = input("Digite a largura da petala:")
dados_flor.append(float(largura_petala))
print(dados_flor)

#CRIANDO UM CLASSIFICADOR
# knn = KNeighborsClassifier(n_neighbors=13)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X,Y)
flor = [6.5,6.5,4.7,1.3]
print(knn.predict([dados_flor]))
# plt.show() 



