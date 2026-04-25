import pandas as pd
import os
from datetime import datetime

def ingest_csv():
    # Simulando um arquivo que chegou de um sistema legado
    source_file = "data_source_legacy.csv"
    save_path = "data_lake/01-bronze-raw"
    
    # Criando um CSV fictício para o teste
    data = {
        "client_name": ["John Doe", "Maria Silva"],
        "document_id": ["888777", "999666"],
        "requested_amount": [5000.00, 12000.50],
        "credit_score": [720, 810]
    }
    pd.DataFrame(data).to_csv(source_file, index=False)

    try:
        print(f"📄 Lendo arquivo CSV: {source_file}")
        df = pd.read_csv(source_file)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"legacy_data_{timestamp}.csv"
        
        df.to_csv(os.path.join(save_path, file_name), index=False)
        print(f"✅ CSV ingerido com sucesso para a Bronze!")
        os.remove(source_file) # Limpa o arquivo temporário
    except Exception as e:
        print(f"❌ Erro no CSV: {e}")

if __name__ == "__main__":
    ingest_csv()