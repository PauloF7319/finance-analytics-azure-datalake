# 🦁 Project: Finance Analytics - The "Lion" Pipeline

This project demonstrates a production-grade data ecosystem engineered for high-security environments, specifically aligned with the **Government Digital and Data Profession Capability Framework**.

## 🏛️ Architectural Evolution & Decision Record

### ☁️ Phase 1: Azure Cloud Validation
Initially designed for **Microsoft Azure** to implement enterprise-level standards:
*   **Storage**: Azure Data Lake Storage Gen2 (Tiers: raw, processed, curated).
*   **Security**: Azure Key Vault for secret management.
*   **Compute**: Azure Databricks for distributed processing.

### 🚀 Phase 2: Strategic Pivot (Local-First & Cost Optimisation)
To maintain high-velocity development with zero operational overhead, the stack transitioned to a **Dockerised environment**. This pivot reflects a real-world engineering challenge: maximising resource efficiency while maintaining full cloud-native compatibility.

### 💎 Phase 3: Silver Layer & Financial Governance
The transformation from **'raw'** to **'processed'** implements rigorous industry standards for data handling:
*   **🛡️ Data Masking & PII Security**: Integrated custom anonymisation logic to protect sensitive customer data (Names and Document IDs), ensuring strict compliance with **GDPR** and Information Assurance protocols.
*   **🔢 Financial Precision**: Systematic rounding to **5 decimal places** for all currency values, catering to high-precision banking product requirements.
*   **💾 Apache Parquet Optimisation**: Transitioned from text-based formats to **Parquet** (columnar storage) for superior performance and compression.
*   **✅ Deduplication**: Implemented logic to handle conflicting records, ensuring a "Single Source of Truth."

---

## 🛠️ Tech Stack & Libraries
*   **Languages**: Python 3.12 (Primary), SQL.
*   **Libraries**: 
    *   `Pandas` & `NumPy`: For complex data manipulation.
    *   `PyArrow`: High-performance Parquet engine.
    *   `Scikit-Learn`: Implementation of Machine Learning models.
    *   `FastAPI`: Simulating Core Banking API systems.
*   **Data Storage**: Apache Parquet, PostgreSQL (Data Warehouse), JSON, CSV.
*   **DevOps & Infrastructure**: Docker, Docker Compose, GitHub Actions (CI/CD).

## 🤖 Machine Learning Integration
The **'curated'** layer incorporates a **Random Forest Classifier** to automate risk assessment:
*   **Prototyping**: Developed an automated risk-scoring model that evaluates creditworthiness.
*   **Deployment**: The model processes the Silver-tier data to generate probability scores, enabling data-driven executive decisions.
*   **Validation**: Performed row-level SQL audits to confirm model accuracy against business thresholds.

## 📊 Business Intelligence & Insights
The pipeline delivers a high-fidelity executive dashboard with the following KPIs:
*   **Total Loan Volume**: £47.22M processed and validated.
*   **Avg Risk Probability**: 35.28% (Calculated via ML inference).
*   **High-Risk Alerts**: 428 records identified for proactive intervention.

## 📈 Pipeline Status
- [x] **'raw'** (Bronze) 🟢
- [x] **'processed'** (Silver) 🟢
- [x] **'curated'** (Gold) & Analytics 🟢 🦁

---
*Developed for Portfolio - Data Engineering & Software Development Standards*