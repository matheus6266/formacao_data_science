

#Importando a biblioteca pandas

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

#---------------------------------------------01 - Dados e Visualização--------------------------------------

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

# Plotando boxsplot 

sns.boxplot(notas.nota)
plt.show()


#--------------------------------------------------------02 - Análise Exploratória (EDA)----------------------------

# Salvando nova arquivo

filmes = pd.read_csv("C:/Users/mathe/OneDrive/Área de Trabalho/Alura/05 - Formação Ciência de Dados/00 - DS Primeiros Passos/data/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]
filmes.head()

# Selecionando todas as avaliações do filmeId 1

notas.query("filmeId == 1")

# Selecionando todas as avaliacoes do filmeId 1 e realizando a média dos valores

notas.query("filmeId == 1").nota.mean()

# Agrupando os valor por filmeId e realizando a média da coluna nota
# Por padrão, no Python usamos "_"

medias_por_filme = notas.groupby("filmeId").mean()["nota"]
medias_por_filme.head()

# Plotando um histograma com a média dos filmes

medias_por_filme.plot(kind = "hist")
plt.show()

# Plotando um boxplot com as médias dos filmes

sns.boxplot(medias_por_filme)
plt.show()

# Pegando as principais métricas

medias_por_filme.describe()

# Plotando o histograma usando o seaborn e alterando o título do gráfico

sns.distplot(medias_por_filme, bins = 10)
plt.title("Histograma das médias dos filmes")
plt.show()

#----------------------------------------------------- Variáveis ------------------------------------------------

# Carregando um novo arquivo

tmdb = pd.read_csv("C:/Users/mathe/OneDrive/Área de Trabalho/Alura/05 - Formação Ciência de Dados/00 - DS Primeiros Passos/data/tmdb_5000_movies.csv")
tmdb.head()

# Visualizando os tipos de linguagem

tmdb.original_language.unique()

#--------------------------------------------------- Data Visualization --------------------------------------

# Criando um df com a soma de cada linguagme

contagem_de_lingua = tmdb["original_language"].value_counts().to_frame()
contagem_de_lingua.head()

# No caso acima teremos um df com uma coluna, sendo que o index será a lingugem
# para retirarmos o index da linguagem e acrescentar uma coluna específica para ele
# devemos fazer o seguinte

contagem_de_lingua = tmdb["original_language"].value_counts().to_frame().reset_index()
contagem_de_lingua.head()

# Mudando o número das variáveis

contagem_de_lingua.columns = ["original_language", "total"]
contagem_de_lingua.head()

# Plotando um gráfico de barras

sns.barplot(x = "original_language", y = "total", data = contagem_de_lingua)
plt.show()

# Plotando o mesmo gráfico, mas sem realizar o cálculos na "mão"

sns.catplot(x = "original_language", kind = "count", data = tmdb)
plt.show()

# Separando os dados

# Somando individualmente por categoria
total_por_lingua = tmdb["original_language"].value_counts()
print(total_por_lingua)
# Somando o total
total_geral = total_por_lingua.sum()
print(total_geral)
# Somando somente a da lingua ingles
total_de_ingles = total_por_lingua.loc["en"]
print(total_de_ingles)
total_do_resto = total_geral - total_de_ingles
print(total_do_resto)

# Printando o valor

print(total_de_ingles, total_do_resto)

# Criando um data frame com os dados fornecidos
# Para rodar o código abaixo eu tenho que selecionar
# toda a linha de comando

dados = {
    "lingua" : ["ingles" , "outros"],
    "total": [total_de_ingles, total_do_resto]
}

dados = pd.DataFrame(dados)
print(dados)

# Plotando o gráfico

sns.barplot(x = "lingua", y = "total", data = dados)
plt.show()

# Separando e contando os filmes que não são em inglês

total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en' ").original_language.value_counts()
total_por_lingua_de_outros_filmes

filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en' ")

# Plotando o gráfico de barras

sns.catplot(x = "original_language", kind = "count", data = filmes_sem_lingua_original_em_ingles)
plt.show()

#---------------------------------------Continuando com visualização-----------------------------------------

# Plotando o gráfico com algumas alterações nas configuracoes dos grafico

sns.catplot(x = "original_language", kind = "count", data = filmes_sem_lingua_original_em_ingles, aspect = 2,
 palette = "GnBu_d", order = total_por_lingua_de_outros_filmes.index)
plt.show()


#----------------------------------- Dados e Estatística ----------------------------------------------------

notas_do_toy_story = notas.query("filmeId == 1")
notas_do_jumanji = notas.query("filmeId == 2")

# Printando as duas médias

print("A nota média do Toy Story %.2f" % notas_do_toy_story.nota.mean())
print("A nota média do Jumanji é %.2f" % notas_do_jumanji.nota.mean())

# Plotando o boxplot

plt.boxplot([notas_do_toy_story.nota, notas_do_jumanji.nota])
plt.show()

# Plotando o mesmo gráfico, mas com o seaborn 

sns.boxplot(x = "filmeId", y = "nota", data = notas.query("filmeId in [1, 2]"))
plt.show()

# Visualizando o desvio padrão

print(notas_do_toy_story.nota.std())
print(notas_do_jumanji.nota.std())