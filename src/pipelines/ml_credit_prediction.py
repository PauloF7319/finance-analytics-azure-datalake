import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Conexão com o Docker
engine = create_engine('postgresql://postgres:password@localhost:5432/finance_db')

def run_credit_ml():
    print("🦁 Iniciando a análise preditiva (Machine Learning)...")
    
    # 1. Extração da Camada Bronze (Raw)
    df = pd.read_sql('SELECT * FROM bronze_raw_data', engine)
    
    # 2. Preparação dos Dados (Features)
    # Não usamos o nome do cliente para o treino, apenas dados numéricos
    X = df[['age', 'annual_income', 'loan_amount', 'credit_score', 'employment_years']]
    y = df['default_risk'] # O que queremos prever
    
    # Dividindo em treino (80%) e teste (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Treinamento do Modelo (Random Forest)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Avaliação
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"✅ Modelo treinado com Precisão de: {acc*100:.2f}%")
    
    # 5. Gerando Predições para TODA a base para o Dashboard
    df['probability_score'] = model.predict_proba(X)[:, 1].round(4) # Probabilidade de risco
    df['prediction_label'] = model.predict(X)
    
    # 6. Salvando na Camada Gold (Curated)
    # Aqui é onde o Dashboard vai buscar os dados finais
    df.to_sql('gold_ml_curated', engine, if_exists='replace', index=False)
    print("🏆 Camada GOLD (Curated) gerada com sucesso para o Dashboard!")

if __name__ == "__main__":
    run_credit_ml()