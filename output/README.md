\# Streaming ETL Pipeline (PySpark + Python)



This project simulates a real-world data engineering workflow using a combination of PySpark, batch ETL, SQL modeling, and Airflow orchestration.  

It is designed to showcase strong DE fundamentals while remaining fully runnable on any machine.



---



\## 📌 Features

\- Ingests raw JSON event data

\- Cleans and transforms data

\- Adds ingestion timestamps

\- Writes curated output to Parquet/CSV

\- Includes a PySpark streaming version (for production-style architecture)

\- Includes a lightweight local ETL version (runnable without Spark)

\- SQL star schema for analytics (fact + dimension tables)

\- Airflow DAG for orchestration



---



\## 📂 Project Structure

streaming-etl-pipeline-pyspark/

│

├── src/

│ ├── streaming\_etl.py # PySpark streaming pipeline (not run on Windows)

│ └── batch\_etl\_local.py # Local ETL pipeline (runs anywhere)

│

├── data/

│ └── raw/events1.json # Sample input data

│

├── output/

│ └── curated/ # ETL output (CSV/Parquet)

│

├── sql/

│ └── create\_star\_schema.sql # Warehouse modeling

│

├── dags/

│ └── streaming\_etl\_dag.py # Airflow DAG

│

└── README.md







---



\## 🚀 How to Run Locally



\### 1. Activate virtual environment  

.venv\\Scripts\\activate



\### 2. Run the ETL pipeline  

python src/batch\_etl\_local.py





Output will appear in `output/curated/events\_curated.csv`.



---



\## 🧠 Why Two ETL Versions?



\### PySpark Version

\- Shows distributed processing concepts

\- Reflects production-style engineering

\- Demonstrates Spark ETL skills



\### Local Python Version

\- Runs on any machine, no Hadoop required

\- Used for testing and demonstration



---



\## 📊 Star Schema



\- \*\*dim\_users\*\*

\- \*\*fact\_events\*\*



Enables analytics such as:

\- user activity breakdown

\- event type analysis

\- spend patterns

\- time-series ingestion insights



---



\## 🛠 Technologies Used

\- Python

\- PySpark (code only)

\- Airflow (DAG structure)

\- SQL (BigQuery-style schema)



---



\## 💡 Author

\*\*Haniya A. Khan\*\*  

Data Engineering \& Analytics Enthusiast



