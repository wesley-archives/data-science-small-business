import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("sorveteria.db")

# cria as consultas
cur_stock = conn.cursor()
cur_sales = conn.cursor()
cur_clients = conn.cursor()
cur_marketing = conn.cursor()

# Executa as consultas SQL
cur_stock.execute("SELECT * FROM stock")
cur_sales.execute("SELECT * FROM sales")
cur_clients.execute("SELECT * FROM clients")
cur_marketing.execute("SELECT * FROM marketing")

# Obter os resultados das consultas
results_stock = cur_stock.fetchall()
results_sales = cur_sales.fetchall()
results_clients = cur_clients.fetchall()
results_marketing = cur_marketing.fetchall()

# Imprimir os resultados das consultas
for result in results_stock:
    print(result)

for result in results_sales:
    print(result)

for result in results_clients:
    print(result)

for result in results_marketing:
    print(result)
