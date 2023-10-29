import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("sorveteria.db")

# importa as bases
stock = pd.read_sql("SELECT * FROM stock", conn)
df = pd.DataFrame(stock)

# Cria o gráfico de colunas para a quantidade de produtos em cada categoria
category_counts = df['categoria'].value_counts()
category_counts.plot(kind='bar')
plt.xlabel('Categoria')
plt.ylabel('Quantidade de Produtos')
plt.title('Quantidade de Produtos em Cada Categoria')
plt.xticks(rotation=45)
plt.tight_layout()

# Salva a imagem no diretório de destino
file_name = 'plt_analysis_columns.png'
diretorio_destino = 'plots/descriptive/'
plt.savefig(f'{diretorio_destino}{file_name}')
