import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("sorveteria.db")

# importa as bases
marketing = pd.read_sql("SELECT * FROM marketing", conn)
df = pd.DataFrame(marketing)

# Cria o gráfico de barras dos investimentos em diferentes meios de campanha
plt.figure(figsize=(10, 6))
plt.bar(df['meio'], df['investimento'])
plt.xlabel('Meio de Campanha')
plt.ylabel('Investimento (R$)')
plt.title('Investimento em Campanhas de Marketing por Meio')
plt.xticks(rotation=45)
plt.tight_layout()

# Salva a imagem no diretório de destino
file_name = 'plt_analysis_bar.png'
diretorio_destino = 'plots/descriptive/'
plt.savefig(f'{diretorio_destino}{file_name}')