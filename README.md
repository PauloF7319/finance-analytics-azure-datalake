# Finance Analytics - Data Lake Architecture & Engineering

This repository demonstrates a complete end-to-end Data Engineering ecosystem, focused on scalability, cost-efficiency, and cloud-readiness.

## 🏗️ Architectural Evolution & Decision Record

### ☁️ Phase 1: Azure Cloud Validation
Initially, the project was deployed on **Microsoft Azure** to implement enterprise-level standards:
- **Storage:** Azure Data Lake Storage Gen2 (Tiers: 01-bronze-raw, 02-silver-processed, 03-gold-curated).
- **Security:** Azure Key Vault for secret management.
- **Compute:** Azure Databricks for distributed processing.
*Evidence of this cloud infrastructure is documented in the `/docs` folder.*

### 🚀 Phase 2: Strategic Pivot (Local-First & Cost Optimization)
To maintain high-velocity development with **zero operational overhead**, I transitioned the stack to a **Dockerized environment**. This pivot reflects a real-world engineering challenge: **maximizing resource efficiency without losing cloud compatibility.**

The architecture now features a custom-built **Source API** (FastAPI) to replace paid third-party data providers, ensuring 100% control over the data contract and ingestion testing.

---

## 🛠️ Tech Stack
- **Languages:** Python 3.12 (venv isolated)
- **API Engine:** FastAPI (Simulating Core Banking systems)
- **Database:** PostgreSQL (Operating as the Data Warehouse)
- **Containerization:** Docker & Docker Compose
- **Data Handling:** Pandas, Psycopg2, Requests
- **Cloud Reference:** Azure (Architecture Design)

---

## 📂 Project Structure & Governance
We follow a strict nomenclature for data layers to ensure governance:
- `data_lake/01-bronze-raw/`: Raw ingestion point (Landing Zone).
- `data_lake/02-silver-processed/`: Cleansed and standardized data.
- `data_lake/03-gold-curated/`: Business-ready aggregates and KPIs.
- `src/api/`: The "Lion" API – A custom FastAPI microservice for data generation.
- `src/utils/`: Modular Python scripts (DB Connectors, Loggers).
- `src/pipelines/`: ETL logic for data movement.

---

## 🦁 Highlights: The Custom "Lion" API
Instead of using static CSVs, I developed a **REST API** to serve as our data source. This allows the pipeline to handle:
1. **Real-time Data Fetching:** Using Python `requests` to simulate live banking transactions.
2. **Dynamic Schema Handling:** Managing JSON responses and mapping them to SQL tables.
3. **Infrastructure as Code:** Everything is orchestrated via Docker Compose, making the environment portable and reproducible.

---
**Status:** 🚧 Developing Ingestion Layer (Bronze)