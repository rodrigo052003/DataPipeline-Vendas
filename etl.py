import pandas as pd
import mysql.connector


# Ler CSV
df = pd.read_csv("dados_vendas.csv")

print(df.head())

# Conexão com MySQL

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rodrigo123",   
    database="vendas_db",
    port=3306     
)

cursor = conn.cursor()

# Inserir dados
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO vendas (data, produto, categoria, regiao, vendas, lucro)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row['Data'],
        row['Produto'],
        row['Categoria'],
        row['Regiao'],
        row['Vendas'],
        row['Lucro']
    ))

conn.commit()
cursor.close()
conn.close()

print("ETL executado com sucesso!")