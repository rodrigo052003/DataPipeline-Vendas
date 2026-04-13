# Data Pipeline de Vendas 📊

Projeto de engenharia de dados que realiza um processo ETL (Extract, Transform, Load) em dados de vendas.

## Funcionalidades
- Leitura de dados de vendas (CSV)
- Limpeza e tratamento dos dados
- Geração de dados organizados para análise

## Tecnologias
- Python
- Pandas
- ETL
- MySQL

## Fluxo do Pipeline
1. Extração: leitura do arquivo de vendas
2. Transformação:
   - remoção de dados inválidos
   - padronização
3. Carga: geração de novo arquivo tratado

## Como executar
```bash
pip install pandas
python etl.py
