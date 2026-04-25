import pandas as pd
import os
from datetime import datetime

def ingest_excel():
    source_file = "finance_report.xlsx"
    save_path = "data_lake/01-bronze-raw"
    
    # Criando um Excel fictício
    data = {
        "client_name": ["Robert Brown"],
        "document_id": ["111222"],
        "requested_amount": [25000.00],
        "credit_score": [650]
    }
    pd.DataFrame(data).to_excel(source_file, index=False)

    try:
        print(f"📊 Lendo planilha Excel: {source_file}")
        df = pd.read_excel(source_file)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"excel_data_{timestamp}.xlsx"
        
        df.to_excel(os.path.join(save_path, file_name), index=False)
        print(f"✅ Excel ingerido com sucesso para a Bronze!")
        os.remove(source_file)
    except Exception as e:
        print(f"❌ Erro no Excel: {e}")

if __name__ == "__main__":
    ingest_excel()