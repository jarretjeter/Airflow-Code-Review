from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
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

@task
def pick_rand_apple(message:str = "Picked apple: ") -> str:
    apple = random.choice(APPLES)
    print(f"{message} " + f"{apple}")


empty_task = EmptyOperator(
    task_id="empty_task"
)


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
    t4 = pick_rand_apple()
    t5 = pick_rand_apple()
    t6 = pick_rand_apple()
    t7 = empty_task
    # for task in range(1, 3):
        
    #     pass


    t1 >> t2 >> t3 >> [t4, t5, t6] >> t7


dag = ch6_code_review_taskflow()