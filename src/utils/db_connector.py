import psycopg2
import sys

def get_connection():
    """
    Estabelece a conexão com o Data Warehouse (PostgreSQL no Docker).
    """
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="finance_analytics",
            user="admin",
            password="finance_pass",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Teste rápido para validar se o Python 'enxerga' o Docker
    print("🔄 Tentando conectar ao banco de dados...")
    connection = get_connection()
    if connection:
        print("✅ Sucesso! O Python e o PostgreSQL estão conversando.")
        connection.close()