from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Funções para as tarefas
def task_1():
    print("Tarefa 1")

def task_2():
    print("Tarefa 2")

# Definindo o DAG
dag = DAG(
    'simple_dag_with_dependencies',
    description='DAG com dependências entre 2 tarefas',
    schedule_interval=None,
    start_date=datetime(2025, 3, 6),
    catchup=False,
)

# Definindo as tarefas
task_1_operator = PythonOperator(
    task_id='task_1',
    python_callable=task_1,
    dag=dag,
)

task_2_operator = PythonOperator(
    task_id='task_2',
    python_callable=task_2,
    dag=dag,
)

# Definindo a dependência entre as tarefas
task_1_operator >> task_2_operator
