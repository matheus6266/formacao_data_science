

#Importando a biblioteca pandas

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


# Carregando o arquivo csv
notas = pd.read_csv("C:/Users/mathe/OneDrive/Área de Trabalho/Alura/05 - Formação Ciência de Dados/00 - DS Primeiros Passos/data/ratings.csv")

# Mostrando os quatro primeiros elementos do arquivo notas
notas.head()

# Mostrando algumas informações sobre os arquivos

notas.shape

# mudando o nome das colunas

notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
notas.head()

# visualizando a coluna notas

notas["nota"] 

# ou

notas.nota

# visualizando a coluna nota com os valores únicos

notas["nota"].unique()

# contando a quantidade de vezes que os valores aparecem 

notas["nota"].value_counts()

# calculando a médias de todas as notas

notas["nota"].mean()

# Plotando um histograma

notas.nota.plot(kind = "hist")
plt.show()

# Visualizando as principais métricas

notas.nota.describe()

sns.boxplot(notas.nota)
plt.show()