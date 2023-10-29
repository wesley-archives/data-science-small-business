import pandas as pd
import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("sorveteria.db")

# importando bases
stock = pd.read_sql("SELECT * FROM stock", conn)
sales = pd.read_sql("SELECT * FROM sales", conn)
clients = pd.read_sql("SELECT * FROM clients", conn)

# Realiza a mesclagem das tabelas
view_sales = pd.merge(sales, clients[['id_cliente', 'nome_cliente']], on='id_cliente', how='left')
view_sales = pd.merge(view_sales, stock[['id_produto', 'nome_produto']], on='id_produto', how='left')

# Remove colunas indesejadas
view_sales = view_sales.drop(['id_cliente', 'id_produto'], axis=1)

# Exporta a tabela combinada para um arquivo CSV
view_sales.to_csv('view_sales_unified.csv', index=False)

# exibe a tabela
print(view_sales)