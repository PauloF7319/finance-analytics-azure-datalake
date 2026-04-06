-- Criação da tabela de aplicações de crédito (Source of Truth)
-- Este script define a estrutura para a nossa camada de Serving/Gold futuramente

CREATE TABLE IF NOT EXISTS credit_applications (
    id SERIAL PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    document_id VARCHAR(20) UNIQUE NOT NULL,
    requested_amount DECIMAL(12, 2) NOT NULL,
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    credit_score INTEGER,
    status VARCHAR(20) -- Approved, Denied, Under Review
);

-- Comentário para o recrutador:
-- 'requested_amount' usa DECIMAL para precisão financeira.
-- 'document_id' possui restrição UNIQUE para evitar duplicidade de registros.