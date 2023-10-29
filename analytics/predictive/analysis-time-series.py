import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("sorveteria.db")

# importa a base
stock = pd.read_sql("SELECT * FROM stock", conn)
df = pd.DataFrame(stock)

# Defina a coluna 'id_produto' como índice
df.set_index('id_produto', inplace=True)

# Plote a série temporal do estoque
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['estoque'])
plt.title('Série Temporal do Estoque ao Longo do Tempo')
plt.xlabel('ID do Produto')
plt.ylabel('Estoque')
plt.grid(True)

# Salva a imagem no diretório de destino
file_name = 'plt_analysis_time_series.png'
diretorio_destino = 'plots/predictive/'
plt.savefig(f'{diretorio_destino}{file_name}')