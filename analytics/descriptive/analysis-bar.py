import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Connect to database
conn = sqlite3.connect("sorveteria.db")

# select the dataframe
marketing = pd.read_sql("SELECT * FROM marketing", conn)
df = pd.DataFrame(marketing)

# Create the graph
plt.figure(figsize=(10, 6))
plt.bar(df['meio'], df['investimento'])
plt.xlabel('Meio de Campanha')
plt.ylabel('Investimento (R$)')
plt.title('Investimento em Campanhas de Marketing por Meio')
plt.xticks(rotation=45)
plt.tight_layout()

# Salve the image
file_name = 'plt_analysis_bar.png'
diretorio_destino = 'plots/descriptive/'
plt.savefig(f'{diretorio_destino}{file_name}')
