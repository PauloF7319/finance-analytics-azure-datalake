# Finance Analytics - Data Lake Architecture

This repository contains an end-to-end Data Engineering project, showcasing a scalable pipeline for financial data analysis.

## 🏗️ Architectural Evolution

### Phase 1: Azure Cloud Setup (Validation)
The initial infrastructure was deployed on **Microsoft Azure** to validate enterprise-grade features:
- **Storage:** Azure Data Lake Storage Gen2 (with Bronze, Silver, and Gold layers).
- **Security:** Azure Key Vault for secret management (managed via RBAC).
- **Compute:** Azure Databricks for PySpark processing.
- **Evidence:** Snapshots of the cloud configuration are stored in `/docs/infrastructure_evidence`.

### Phase 2: Strategic Pivot to Local-First (Cost Optimization & Full Control)
To ensure high-velocity development with **zero operational costs**, the project transitioned to a **Dockerized environment**. We implemented a custom **Source API** to eliminate dependency on paid third-party providers, ensuring 100% availability for testing complex ETL logic and error handling.

## 🛠️ Tech Stack (Current)
- **Language:** Python 3.12 (Venv isolated)
- **Database:** PostgreSQL (Serving as the Data Warehouse)
- **API Source:** FastAPI (Custom-built microservice for real-time credit data simulation)
- **Data Manipulation:** Pandas & Psycopg2
- **Infrastructure:** Docker & Docker Compose
- **Version Control:** Git (Local-first with cloud mirroring)

## 📂 Project Structure
- `data_lake/`: Local simulation of ADLS Gen2 tiers (**01-bronze-raw**, **02-silver-processed**, **03-gold-curated**).
- `src/api/`: Custom FastAPI source representing a Core Banking system.
- `src/utils/`: Modular Python utilities (e.g., Database Connectors).
- `src/pipelines/`: Ingestion and transformation scripts.
- `sql_scripts/`: DDL and DML scripts for PostgreSQL schema management.
- `docs/`: Architecture diagrams and cloud infrastructure evidence.

## 🚀 Current Progress: The "Lion" API
We have successfully deployed a **FastAPI container** that generates synthetic credit applications. This allows us to test:
1. **API Connectivity:** Handling REST requests locally.
2. **Data Consistency:** Mapping JSON responses to Relational Schemas.
3. **Resilience:** Building a pipeline that survives platform outages or credential rotations.