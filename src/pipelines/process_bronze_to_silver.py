import pandas as pd
import glob
import os
from datetime import datetime

def mask_sensitive_data(df):
    """
    Aplica mascaramento em dados sensíveis (PII) para conformidade com GDPR/LGPD.
    """
    # Mascarando Nomes: Mantém a primeira letra e oculta o resto
    if 'client_name' in df.columns:
        df['client_name'] = df['client_name'].apply(
            lambda x: str(x)[0] + '*' * (len(str(x)) - 1) if pd.notnull(x) and len(str(x)) > 0 else x
        )
    
    # Mascarando Documentos: Mantém os 3 primeiros caracteres
    if 'document_id' in df.columns:
        df['document_id'] = df['document_id'].apply(
            lambda x: str(x)[:3] + '*' * (len(str(x)) - 3) if pd.notnull(x) and len(str(x)) > 3 else x
        )
    
    return df

def process_data():
    # Definição das camadas conforme nossa nomenclatura de governança
    bronze_path = "data_lake/01-bronze-raw"
    silver_path = "data_lake/02-silver-processed"
    
    print(f"🔍 Iniciando processamento: {bronze_path} -> {silver_path}")
    
    # Busca todos os arquivos na camada raw
    all_files = glob.glob(os.path.join(bronze_path, "*.*"))
    combined_data = []

    for file in all_files:
        try:
            if file.endswith(".json"):
                df = pd.read_json(file)
            elif file.endswith(".csv"):
                df = pd.read_csv(file)
            elif file.endswith(".xlsx"):
                df = pd.read_excel(file)
            else:
                continue
            combined_data.append(df)
            print(f"✅ Arquivo lido com sucesso: {os.path.basename(file)}")
        except Exception as e:
            print(f"❌ Falha ao ler {file}: {e}")

    if not combined_data:
        print("⚠️ Nenhum dado encontrado para processar.")
        return

    # Consolidação dos dados (The "T" in ETL)
    full_df = pd.concat(combined_data, ignore_index=True)

    # 1. SEGURANÇA: Mascaramento de dados sensíveis
    full_df = mask_sensitive_data(full_df)

    # 2. PRECISÃO FINANCEIRA: Arredondamento para 5 casas decimais
    if 'requested_amount' in full_df.columns:
        full_df['requested_amount'] = full_df['requested_amount'].astype(float).round(5)
    
    # 3. QUALIDADE: Deduplicação (evita registros repetidos de sistemas diferentes)
    full_df = full_df.drop_duplicates(subset=['document_id'], keep='last')
    
    # 4. AUDITORIA: Registro do momento do processamento
    full_df['processed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Criar pasta silver se não existir
    os.makedirs(silver_path, exist_ok=True)
    
    # 5. ARMAZENAMENTO: Salvando no formato Apache Parquet (Padrão Big Data)
    timestamp = datetime.now().strftime("%Y%m%d")
    output_file = os.path.join(silver_path, f"processed_credit_data_{timestamp}.parquet")
    
    full_df.to_parquet(output_file, index=False)
    
    print(f"\n🏆 Pipeline Silver finalizado!")
    print(f"📊 Registros totais: {len(full_df)}")
    print(f"💾 Arquivo gerado: {output_file}")

if __name__ == "__main__":
    process_data()