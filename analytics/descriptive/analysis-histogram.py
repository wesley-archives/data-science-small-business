import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("sorveteria.db")

# importando bases
clients = pd.read_sql("SELECT * FROM clients", conn)
df = pd.DataFrame(clients)

# Define a idade dos clientes
today = datetime.today()
df['data_nascimento'] = pd.to_datetime(df['data_nascimento'])
df['idade'] = today.year - df['data_nascimento'].dt.year

# Histograma de idades
plt.hist(df['idade'], bins=10, edgecolor='k')
plt.title('Distribuição de Idades dos Clientes')
plt.xlabel('Idade')
plt.ylabel('Número de Clientes')

# Salva a imagem no diretório de destino
file_name = 'plt_analysis_histogram.png'
diretorio_destino = 'plots/descriptive/'
plt.savefig(f'{diretorio_destino}{file_name}')