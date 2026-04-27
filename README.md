# Finance Analytics - Data Lake Architecture & Engineering 🦁

This repository demonstrates a complete end-to-end Data Engineering ecosystem, focused on scalability, financial precision, and data privacy.

## 🏗️ Architectural Evolution & Decision Record

### ☁️ Phase 1: Azure Cloud Validation
Initially designed for **Microsoft Azure** to implement enterprise-level standards:
* **Storage:** Azure Data Lake Storage Gen2 (Tiers: raw, processed, curated).
* **Security:** Azure Key Vault for secret management.
* **Compute:** Azure Databricks for distributed processing.

### 🚀 Phase 2: Strategic Pivot (Local-First & Cost Optimization)
To maintain high-velocity development with zero operational overhead, the stack was transitioned to a **Dockerized environment**. This pivot reflects a real-world engineering challenge: maximizing resource efficiency without losing cloud compatibility.

### 💎 Phase 3: Silver Layer & Financial Governance
The transformation from `01-bronze-raw` to `02-silver-processed` implements rigorous industry standards:

* **🛡️ Data Masking & PII Security:** Integrated custom anonymization logic to protect sensitive customer data (Names and Document IDs), ensuring compliance with **GDPR** standards even in analytical environments.
* **🔢 Financial Precision:** Systematic rounding to **5 decimal places** for all currency values, catering to high-precision FX and banking product requirements.
* **💾 Apache Parquet Optimization:** Transitioned from text-based formats to **Parquet**, leveraging columnar storage for superior compression and significant performance gains.
* **✅ Deduplication:** Implemented logic to handle conflicting records across different source systems, ensuring a "Single Source of Truth."

## 🛠️ Tech Stack
* **Languages:** Python 3.12 (venv isolated)
* **Data Storage & Formats:** Apache Parquet (Standard for Big Data), JSON, CSV, XLSX.
* **Data Handling:** Pandas, PyArrow (Parquet engine), Openpyxl.
* **API Engine:** FastAPI (Simulating Core Banking systems).
* **Database:** PostgreSQL (Operating as the Data Warehouse).
* **Containerization:** Docker & Docker Compose.

## 📂 Project Structure & Governance
* `data_lake/01-bronze-raw/`: Multimodal ingestion point (JSON, CSV, XLSX).
* `data_lake/02-silver-processed/`: Cleansed, masked, and standardized data in **Parquet** format.
* `data_lake/03-gold-curated/`: Business-ready aggregates and KPIs (In development).
* `src/pipelines/`: ETL/ELT logic for data movement and refinement.

## 🦁 Highlights: The "Lion" Pipeline
Instead of using static data, this project handles a **Hybrid Ingestion** model, processing real-time API calls alongside legacy filesystem exports. The pipeline is **Source Agnostic**, meaning it can ingest and standardize data regardless of the original format.

**Status:** ✅ Ingestion Layer (Bronze) Completed | ✅ Silver Layer (Processing) Completed | 🚧 Developing Gold Layer (Analytics)