import pandas as pd
import os
from datetime import datetime

def generate_gold_layer():
    silver_path = "data_lake/02-silver-processed"
    gold_path = "data_lake/03-gold-curated"
    
    print(f"🚀 Gerando indicadores Gold para Dashboard...")
    
    # Busca o arquivo Parquet consolidado na Silver
    files = [f for f in os.listdir(silver_path) if f.endswith('.parquet')]
    if not files:
        print("⚠️ Silver vazia. Rode o pipeline de refino primeiro.")
        return
    
    latest_file = os.path.join(silver_path, sorted(files)[-1])
    df = pd.read_parquet(latest_file)
    
    # 1. Definindo as categorias de risco baseadas no score
    bins = [0, 500, 700, 850, 1000]
    labels = ['High Risk', 'Medium Risk', 'Good', 'Excellent']
    df['risk_category'] = pd.cut(df['credit_score'], bins=bins, labels=labels)
    
    # 2. Agregação por Região e Categoria (O coração do Heatmap)
    gold_summary = df.groupby(['region', 'risk_category'], observed=False).agg({
        'document_id': 'count',
        'requested_amount': 'sum'
    }).reset_index()
    
    # Renomeando para facilitar a vida no Power BI
    gold_summary.columns = ['Region', 'Risk_Level', 'Total_Applications', 'Total_Volume_GBP']
    
    # Mantendo a precisão de 5 casas decimais
    gold_summary['Total_Volume_GBP'] = gold_summary['Total_Volume_GBP'].round(5)

    # 3. Salvando o arquivo final de Analytics
    os.makedirs(gold_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d")
    output_file = os.path.join(gold_path, f"gold_financial_insights_{timestamp}.parquet")
    
    gold_summary.to_parquet(output_file, index=False)
    
    print(f"🏆 Camada GOLD finalizada com {len(gold_summary)} insights regionais!")
    print(f"💾 Caminho: {output_file}")
    print("\n--- Amostra dos Dados para o Dashboard ---")
    print(gold_summary.head(10))

if __name__ == "__main__":
    generate_gold_layer()