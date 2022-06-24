from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime
import random


APPLES = ["pink lady", "jazz", "orange pippin", "granny smith", "red delicious", "gala", "honeycrisp", "mcintosh", "fuji"]

# simple bash operator to 'echo' or print my name to a txt file in the dags directory
echo_to_file = BashOperator(
task_id="echo_to_file",
# use full filepath for a local airflow instance
bash_command="echo Jarret > /home/jarret/data-engineering-bootcamp/workspace/airflow-code-review/dags/ch6_code_review.txt"
)


# @task is a python decorator that can be used to declare that the function is to be used as a DAG task. Can be used in the place of a python operator for simplicity and better readability
@task
def print_hello() -> str:
    """
    Reads a text file and prints a greeting message along with the content of the file (my name)
    """
    with open("/home/jarret/data-engineering-bootcamp/workspace/airflow-code-review/dags/ch6_code_review.txt", "r") as file:
        text = file.read()
        print(f"Hello, {text}!")


# Another bash operator using a bash command to have the task echo a string
echo_msg = BashOperator(
task_id="echo_msg",
bash_command="echo picking three random apples"
)


@task
def pick_rand_apple(message:str = "Picked apple: ") -> str:
    """
    Calls the 'random' module's '.choice' method to retrieve one of the apples from the APPLES list, printing the value along with a message.
    """
    apple = random.choice(APPLES)
    print(f"{message} " + f"{apple}")

# Does nothing. Used for practice
empty_task = EmptyOperator(
    task_id="empty_task"
)

# instantiating a function as a DAG and configuring it
@dag(
    schedule_interval="@once",
    start_date=datetime.utcnow(),
    catchup=False,
    default_view="graph",
    is_paused_upon_creation=True,
    tags=["code_review"]
)
def ch6_code_review_taskflow():
    """
    DAG to run all of the above defined tasks. Assign them to variables t1-t7 for less typing when specifying the run order.
    """
    t1 = echo_to_file
    t2 = print_hello()
    t3 = echo_msg
    t4 = pick_rand_apple()
    t5 = pick_rand_apple()
    t6 = pick_rand_apple()
    t7 = empty_task

    # Defining the workflow order of all tasks. Tasks 4-6 are grouped to run at the same time and task 7 only runs after they all complete successfully. 
    t1 >> t2 >> t3 >> [t4, t5, t6] >> t7

# Running the function as a DAG
dag = ch6_code_review_taskflow()