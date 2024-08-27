from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'nvlong',
    'start_date': datetime(2024, 1, 25),
    'catchup': False
}

dag = DAG(
    'first-dag',
    default_args = default_args,
    schedule=timedelta(days=1)
)

t1 = BashOperator(
    task_id = 'hello_world',
    bash_command='echo "Hello World"',
    dag = dag
)

t2 = BashOperator(
    task_id = 'hello_dml',
    bash_command='echo "Hello 1234566"',
    dag = dag
)

t1 >> t2