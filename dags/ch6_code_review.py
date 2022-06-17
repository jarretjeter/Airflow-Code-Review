from airflow import DAG
# from airflow.operators import dag, task
from airflow.operators.bash import BashOperator
from datetime import datetime
import random
import time

APPLES = ["pink lady", "jazz", "orange pippin", "granny smith", "red delicious", "gala", "honeycrisp", "mcintosh", "fuji"]

default_args = {
    "schedule_interval": "@once",
    "start_date": datetime.utcnow(),
    "catchup": False,
    "default_view": "graph",
    "is_paused_upon_creation": True,
    "tags": ["code_review"]
}

with DAG(
    "code_review",
    description="bash operator to echo name output to file",
    default_args=default_args
) as dag:

    echo_to_file = BashOperator(
        task_id="echo_name",
        # NAME="Jarret",
        bash_command="echo Jarret > echo Jarret > /home/jarret/data-engineering-bootcamp/workspace/airflow-code-review/dags/ch6_code_review.txt"
        )

# @dag(
#     schedule_interval="@once",
#     start_date=datetime.utcnow(),
#     catchup=False,
#     default_view="graph",
#     is_paused_upon_creation=True,
#     tags=["code_review"]
# )

echo_to_file