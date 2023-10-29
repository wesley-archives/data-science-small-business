import pandas as pd
import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("sorveteria.db")

# importa a base
clients = pd.read_sql("SELECT * FROM clients", conn)
df = pd.DataFrame(clients)

# Exibe as primeiras 5 linhas do DataFrame
print(df.head())

# Resumo estatístico das colunas numéricas
print(df.describe())