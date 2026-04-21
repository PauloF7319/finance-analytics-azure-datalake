import json
import os
from datetime import datetime

import requests


def ingest_from_api():
    api_url = "http://localhost:8000/v1/credit-applications"
    save_path = "data_lake/01-bronze-raw"
    
    try:
        print(f"🦁 Chamando o Leão em {api_url}...")
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"transaction_{timestamp}.json"
        full_path = os.path.join(save_path, file_name)
        
        os.makedirs(save_path, exist_ok=True)
        
        with open(full_path, 'w') as f:
            json.dump(data, f, indent=4)
            
        print(f"✅ Sucesso! Dado salvo em: {full_path}")
        
    except Exception as e:
        print(f"❌ Erro: {e}. Verifique se o Docker/API está rodando!")

if __name__ == "__main__":
    ingest_from_api()