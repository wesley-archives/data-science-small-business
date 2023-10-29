import pandas as pd

sales = pd.read_csv('sheets/originals/Vendas.csv')
clients = pd.read_csv('sheets/originals/Clientes.csv')
stock = pd.read_csv('sheets/originals/Estoque.csv')
marketing = pd.read_csv('sheets/originals/Marketing.csv')

# Remove colunas vazias
sales = sales.dropna(axis=1)
clients = clients.dropna(axis=1)
stock = stock.dropna(axis=1)
marketing = marketing.dropna(axis=1)

# Renomeia as colunas
sales.columns = ['id', 'data_venda', 'id_cliente', 'id_produto', 'quantidade', 'total']
clients.columns = ['id_cliente', 'nome_cliente', 'genero', 'data_nascimento', 'email', 'telefone', 'endereco', 'cidade', 'estado', 'cep']
stock.columns = ['id_produto', 'nome_produto', 'categoria', 'estoque', 'custo_unitario', 'custo_total', 'preco_venda', 'total_estoque']
marketing.columns = ['id_campanha', 'meio', 'investimento', 'roi', 'custos', 'alcance']

# Limpa colunas removendo o símbolo de moeda e transformando em float
sales['total'] = sales['total'].str.replace('R$', '').str.replace(',', '.', regex=True).astype(float)

# Converte colunas para o tipo datetime
sales['data_venda'] = pd.to_datetime(sales['data_venda'])
clients['data_nascimento'] = pd.to_datetime(clients['data_nascimento'])

# Exporta o DataFrame limpo
sales.to_csv('sheet_sales.csv', index=False)
clients.to_csv('sheet_clients.csv', index=False)
stock.to_csv('sheet_stock.csv', index=False)
marketing.to_csv('sheet_marketing.csv', index=False)