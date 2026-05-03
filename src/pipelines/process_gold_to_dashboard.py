import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:password@localhost:5432/finance_db')

def create_star_schema():
    print("🦁 Organizando os dados para o Power BI (Star Schema)...")
    
    # Lendo os dados da camada Gold que o ML gerou
    df = pd.read_sql('SELECT * FROM gold_ml_curated', engine)
    
    # 1. Tabela de Dimensão: Clientes (Contexto)
    dim_clients = df[['client_name', 'age', 'employment_years']].copy()
    dim_clients['client_key'] = range(1, len(dim_clients) + 1)
    
    # 2. Tabela de Fatos: Crédito e Predições (Métricas)
    fact_credit = df[['annual_income', 'loan_amount', 'credit_score', 'probability_score', 'prediction_label']].copy()
    fact_credit['client_key'] = dim_clients['client_key']
    
    # Salvando tabelas específicas para o BI ler
    dim_clients.to_sql('dim_clients', engine, if_exists='replace', index=False)
    fact_credit.to_sql('fact_credit_predictions', engine, if_exists='replace', index=False)
    
    print("✅ Star Schema pronto no Postgres! Dimensões e Fatos criadas.")

if __name__ == "__main__":
    create_star_schema()