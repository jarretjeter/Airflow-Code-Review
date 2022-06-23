from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from datetime import datetime
import random
import time

APPLES = ["pink lady", "jazz", "orange pippin", "granny smith", "red delicious", "gala", "honeycrisp", "mcintosh", "fuji"]


echo_to_file = BashOperator(
task_id="echo_to_file",
# NAME="Jarret",
bash_command="echo Jarret > /home/jarret/data-engineering-bootcamp/workspace/airflow-code-review/dags/ch6_code_review.txt"
)


@task
def print_hello():
    with open("/home/jarret/data-engineering-bootcamp/workspace/airflow-code-review/dags/ch6_code_review.txt", "r") as file:
        text = file.read()
        print(f"Hello, {text}!")


echo_msg = BashOperator(
task_id="echo_msg",
bash_command="echo picking three random apples"
)

# for task in range(4, 7):
# @task
# def rand_apple_task4(message:str) -> str:
#     for apple in range(len(APPLES) -1):
        

@dag(
    schedule_interval="@once",
    start_date=datetime.utcnow(),
    catchup=False,
    default_view="graph",
    is_paused_upon_creation=True,
    tags=["code_review"]
)
def ch6_code_review_taskflow():

    t1 = echo_to_file
    t2 = print_hello()
    t3 = echo_msg



    t1 >> t2 >> t3


dag = ch6_code_review_taskflow()