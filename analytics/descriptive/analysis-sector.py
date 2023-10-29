import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("sorveteria.db")

# importa a base
clients = pd.read_sql("SELECT * FROM clients", conn)
df = pd.DataFrame(clients)

# Gráfico de pizza de gêneros
gender_counts = df['genero'].value_counts()
gender_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição de Gênero dos Clientes')
plt.axis('equal')

# Salva a imagem no diretório de destino
file_name = 'plt_analysis_sector.png'
diretorio_destino = 'plots/descriptive/'
plt.savefig(f'{diretorio_destino}{file_name}')