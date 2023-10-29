import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("sorveteria.db")

# importa a base
marketing = pd.read_sql("SELECT * FROM marketing", conn)
df = pd.DataFrame(marketing)

# indexa as variaveis de estudo
x = df[['custos']]
y = df['alcance']

# Criando e treinando o modelo de regressão linear
model = LinearRegression()
model.fit(x, y)

# Realizando previsões
previsoes = model.predict(x)

# Cria o gráfico de dispersão
plt.scatter(x, y, color='blue')
plt.plot(x, previsoes, color='red', linewidth=2)
plt.xlabel('Investimento em Publicidade (R$)')
plt.ylabel('Vendas (R$)')
plt.title('Regressão Linear: Investimento em Publicidade vs. Vendas')
plt.grid(True)

# Salva a imagem no diretório de destino
file_name = 'plt_analysis_regression.png'
diretorio_destino = 'plots/predictive/'
plt.savefig(f'{diretorio_destino}{file_name}')