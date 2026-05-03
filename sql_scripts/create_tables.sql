DROP TABLE IF EXISTS silver_credit_data;

CREATE TABLE silver_credit_data (
    document_id VARCHAR(50) PRIMARY KEY,
    client_name VARCHAR(100),
    region VARCHAR(50), 
    credit_score INT,
    requested_amount NUMERIC(20, 5),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);