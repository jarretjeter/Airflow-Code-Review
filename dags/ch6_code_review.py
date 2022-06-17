from unicodedata import name
from airflow import DAG
from airflow.operators import dag, task
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
    "ch6_code_review",
    description="bash operator to echo name output to file",
    default_args=default_args
) as dag:

    echo_to_file = BashOperator(
        task_id="echo_name",
        name = "Jarret",
        bash_command=f"echo {name} > ch6_code_review.txt"
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