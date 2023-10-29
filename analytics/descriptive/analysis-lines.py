import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("sorveteria.db")

# importa a base
sales = pd.read_sql("SELECT * FROM sales", conn)
df = pd.DataFrame(sales)

# Remove a hora da coluna "data_venda"
df['data_venda'] = pd.to_datetime(df['data_venda']).dt.date

# Agrega o total de vendas por dia
daily_sales = df.groupby('data_venda')['total'].sum()

# Cria o gráfico de linhas para representar a evolução das vendas ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-')
plt.xlabel('Data da Venda')
plt.ylabel('Total de Vendas (R$)')
plt.title('Evolução das Vendas ao Longo do Tempo')
plt.grid(True)
plt.tight_layout()

# Salva a imagem no diretório de destino
file_name = 'plt_analysis_lines.png'
diretorio_destino = 'plots/descriptive/'
plt.savefig(f'{diretorio_destino}{file_name}')