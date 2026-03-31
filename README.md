Azure Finance Analytics - Open Banking Data Pipeline
📖 Project Overview
This project demonstrates the development of a high-performance, secure data ecosystem on Azure, specifically designed for the ingestion and processing of Open Finance data. The primary objective is to apply Data Engineering principles within a realistic financial scenario, ensuring robust governance, scalability, and absolute data integrity.

🏗️ Architecture and Technical Decisions
1. Cloud Infrastructure (Azure)
Region: UK South (London).

Rationale: A strategic choice to ensure compliance with UK financial regulations and to provide low-latency connectivity for global banking services.

Resource Group: rg-finance-analytics-raw-processed – Centralised organisation for cost control and resource lifecycle management.

2. Storage and Governance (Data Lake Gen2)
Implementation of an Azure Data Lake Storage Gen2 focusing on performance and structural integrity:

Hierarchical Namespace (HNS): Enabled. This transforms object storage into a true file system, allowing for high-performance metadata operations and granular security via ACLs.

Medallion Architecture (Standard Nomenclature):

01_bronze_raw: Original data from the API (JSON/CSV) kept in its immutable, raw state.

02_silver_processed: Cleaned, typed data with rigorous quality rules applied.

03_gold_curated: Highly aggregated data, modelled for business consumption (Power BI/Analytics).

3. Security and Identity
Authentication: Exclusive use of Service Principals (App Registration) for inter-service communication.

Security: Assignment of the Storage Blob Data Contributor role to the Service Principal, adhering to the Principle of Least Privilege to avoid exposing account-level master keys.

🛠️ Data Quality (Data Stewardship)
The pipeline is designed to handle common data anomalies in the financial sector with professional rigour:

Name Standardisation: String normalisation (Title Case) to ensure consistency across reports.

Handling Nulls: Financial nulls are treated with fillna(0) to protect sum calculations, while missing names are flagged as UNKNOWN CLIENT.

Chronological Rigour: Unification of multiple date formats into the ISO standard (YYYY-MM-DD).

Integrity Checks: Automated row count validation processes between the Bronze and Silver layers.

🚀 Next Steps
[x] Azure Infrastructure Configuration (Data Lake & HNS).

[x] Layer Governance Definition (Bronze, Silver, Gold).

[ ] Implementation of API Ingestion Notebook (Open Banking).

[ ] Data Cleansing Automation using PySpark/Pandas.