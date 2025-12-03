-- Dimension table for users
CREATE TABLE dim_users (
    user_id STRING,
    signup_date DATE,
    country STRING
);

-- Fact table for events
CREATE TABLE fact_events (
    event_id STRING,
    user_id STRING,
    event_type STRING,
    amount FLOAT64,
    event_ts TIMESTAMP,
    ingest_ts TIMESTAMP
);
