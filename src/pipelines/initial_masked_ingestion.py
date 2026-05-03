import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Conexão unificada (Docker Postgres)
engine = create_engine('postgresql://postgres:password@localhost:5432/finance_db')

def apply_mask(name):
    # Garante as 3 primeiras letras e mascara o restante
    name_str = str(name)
    if len(name_str) > 3:
        return name_str[:3] + "*" * (len(name_str) - 3)
    return name_str + "***"

def generate_masked_data(records=1000):
    print(f"🚀 Generando exatamente {records} registros mascarados...")
    
    np.random.seed(42)
    
    # Gerando nomes fictícios compostos para mascarar
    first_names = ['James', 'Mary', 'Robert', 'Patricia', 'John', 'Jennifer', 'Michael', 'Linda']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis']
    
    # Criando a lista de 1000 nomes e aplicando a máscara imediatamente
    raw_names = [f"{np.random.choice(first_names)} {np.random.choice(last_names)}" for _ in range(records)]
    masked_names = [apply_mask(n) for n in raw_names]
    
    data = {
        'client_name': masked_names,
        'age': np.random.randint(18, 75, size=records),
        'annual_income': np.random.uniform(20000, 150000, size=records).round(2),
        'loan_amount': np.random.uniform(5000, 90000, size=records).round(2),
        'credit_score': np.random.randint(300, 850, size=records),
        'employment_years': np.random.randint(0, 40, size=records)
    }
    
    df = pd.DataFrame(data)
    
    # Criando o alvo para o ML (Risco de Inadimplência)
    # Lógica: Score < 500 e Empréstimo > 50% da Renda = Risco (1)
    condition = (df['credit_score'] < 500) & (df['loan_amount'] > df['annual_income'] * 0.5)
    df['default_risk'] = np.where(condition, 1, 0)

    # Ingestão na camada RAW (Bronze)
    df.to_sql('bronze_raw_data', engine, if_exists='replace', index=False)
    print(f"✅ Sucesso! Tabela 'bronze_raw_data' pronta com {len(df)} registros.")

if __name__ == "__main__":
    generate_masked_data()