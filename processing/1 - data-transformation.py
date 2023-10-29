import pandas as pd

# Lê a planilha Excel
base = pd.ExcelFile('sheets/originals/sorveteria-doce-gosto.xlsx')

# Obtem a lista de nomes das abas ou planilhas no arquivo Excel
abas = base.sheet_names

# Para cada aba, lê os dados e salva como CSV
for aba in abas:
    df = base.parse(aba)
    nome_arquivo_csv = f'{aba}.csv'
    df.to_csv(nome_arquivo_csv, index=False)

print("Conversão concluída. Arquivos CSV gerados com sucesso.")
