import sqlite3
import pandas as pd

# Criar um banco de dados SQLite
conn = sqlite3.connect('sorveteria.db')

# Importa os arquivos csv
stock = 'sheets/transformed/sheet_stock.csv'
sales = 'sheets/transformed/sheet_sales.csv'
clients = 'sheets/transformed/sheet_clients.csv'
marketing = 'sheets/transformed/sheet_marketing.csv'

# transforma as bases em dataframes
df_stock = pd.read_csv(stock)
df_sales = pd.read_csv(sales)
df_clients = pd.read_csv(clients)
df_marketing = pd.read_csv(marketing)

# Exporta os dataframes para o banco de dados
df_stock.to_sql('stock', conn, if_exists='replace')
df_sales.to_sql('sales', conn, if_exists='replace')
df_clients.to_sql('clients', conn, if_exists='replace')
df_marketing.to_sql('marketing', conn, if_exists='replace')