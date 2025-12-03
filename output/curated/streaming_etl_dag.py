from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "haniya",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="etl_pipeline_batch",
    default_args=default_args,
    description="Batch ETL pipeline orchestration",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
):

    run_batch_etl = BashOperator(
        task_id="run_batch_etl",
        bash_command="python src/batch_etl_local.py"
    )

    run_batch_etl
