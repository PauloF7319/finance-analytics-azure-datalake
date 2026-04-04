from fastapi import FastAPI
import random
from datetime import datetime

app = FastAPI()

@app.get("/v1/credit-applications")
def get_credit_data():
    # Simulando um "leão": uma API que gera dados de pedidos de crédito
    statuses = ["APPROVED", "REJECTED", "PENDING_MANUAL_REVIEW"]
    return {
        "application_id": f"APP-{random.randint(1000, 9999)}",
        "client_id": f"CUST-{random.randint(1, 500)}",
        "requested_amount": round(random.uniform(1000, 50000), 2),
        "status": random.choice(statuses),
        "timestamp": datetime.now().isoformat()
    }