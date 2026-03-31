# Finance Analytics - Data Lake Architecture

This repository contains an end-to-end Data Engineering project, showcasing a scalable pipeline for financial data analysis.

## 🏗️ Architectural Evolution

### Phase 1: Azure Cloud Setup (Validation)
The initial infrastructure was deployed on **Microsoft Azure** to validate enterprise-grade features:
- **Storage:** Azure Data Lake Storage Gen2 (with Bronze, Silver, and Gold layers).
- **Security:** Azure Key Vault for secret management (managed via RBAC).
- **Compute:** Azure Databricks for PySpark processing.
- **Evidence:** Snapshots of the cloud configuration are stored in `/docs/infrastructure_evidence`.

### Phase 2: Strategic Pivot to Local-First (Cost Optimization)
To ensure high-velocity development with zero operational costs, the project transitioned to a **Dockerized environment**. This approach simulates the cloud ecosystem locally, ensuring the ETL logic remains 100% cloud-ready while optimizing resource usage.

## 🛠️ Tech Stack (Current)
- **Language:** Python (PySpark)
- **Orchestration:** Apache Airflow (Dockerized)
- **Database:** PostgreSQL (simulating on-premise sources)
- **Infrastructure:** Docker & Docker Compose
- **Version Control:** Git

## 📂 Project Structure
- `docs/`: Architecture diagrams and cloud infrastructure evidence.
- `dags/`: Airflow Directed Acyclic Graphs for orchestration.
- `spark/`: Transformation scripts (Raw to Curated).