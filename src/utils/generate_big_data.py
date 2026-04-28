import pandas as pd
import random
import os

def generate_mock_data(records=200):
    # Regiões estratégicas do Reino Unido
    regions = [
        'Greater London', 'South East', 'North West', 
        'West Midlands', 'East Midlands', 'Scotland', 
        'Wales', 'East of England', 'South West'
    ]
    
    names = ['John', 'Mary', 'Robert', 'Patricia', 'Michael', 'Linda', 'William', 'Elizabeth', 'David', 'Barbara']
    surnames = ['Smith', 'Jones', 'Taylor', 'Brown', 'Williams', 'Wilson', 'Johnson', 'Davies', 'Robinson', 'Wright']

    data = []
    for i in range(records):
        data.append({
            'document_id': f"{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(10, 99)}",
            'client_name': f"{random.choice(names)} {random.choice(surnames)}",
            'region': random.choice(regions),
            'credit_score': random.randint(300, 850),
            'requested_amount': round(random.uniform(5000, 75000), 5) # Aumentei o teto para dar mais variedade
        })

    df = pd.DataFrame(data)
    
    # Caminho da Bronze
    bronze_path = 'data_lake/01-bronze-raw'
    os.makedirs(bronze_path, exist_ok=True)
    
    # Distribuindo para mostrar que o pipeline é híbrido
    df.iloc[:70].to_json(f'{bronze_path}/api_bulk_data.json', orient='records', indent=4)
    df.iloc[70:140].to_csv(f'{bronze_path}/legacy_system_data.csv', index=False)
    df.iloc[140:].to_excel(f'{bronze_path}/manual_spreadsheet_data.xlsx', index=False)
    
    print(f"✅ Sucesso! {records} registros gerados.")
    print(f"📍 Regiões incluídas: {', '.join(regions)}")

if __name__ == "__main__":
    generate_mock_data()