import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os

def load_data():
    # Configurações de conexão (Docker)
    conn_string = "postgresql://user:password@localhost:5432/finance_db"
    engine = create_engine(conn_string)
    
    silver_path = "data_lake/02-silver-processed"
    
    # 1. Busca o arquivo Parquet mais recente
    files = [f for f in os.listdir(silver_path) if f.endswith('.parquet')]
    if not files:
        print("⚠️ Nenhum arquivo Parquet encontrado na Silver.")
        return
    
    latest_file = os.path.join(silver_path, sorted(files)[-1])
    df = pd.read_parquet(latest_file)
    
    print(f"🚀 Carregando {len(df)} registros para o PostgreSQL...")
    
    # 2. Carga para o Banco (Substitui os dados antigos)
    try:
        df.to_sql('silver_credit_data', engine, if_exists='replace', index=False)
        print("✅ Dados carregados com sucesso no banco de dados!")
    except Exception as e:
        print(f"❌ Erro na carga: {e}")

if __name__ == "__main__":
    load_data()