from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import datetime
from pathlib import Path

data_lake_path = Path(__file__).parents[1] / "data" / "datalake"
data_warehouse_path = Path(__file__).parents[1] / "data" / "data_warehouse"
# .as_posix() not needed since script wiill be run in docker container which is Linux (will not work outside though)

time_variable = "$(date +%y%m%d_%H%M%S)"

with DAG(dag_id = "joke_DAG", start_date=datetime(2023,8,8)):
    say_hello = BashOperator(task_id = "say_hello", bash_command="echo 'hej hej jokeing time'")

    setup_folders = BashOperator(task_id = "setup_folders", bash_command=f"mkdir -p {data_lake_path} {data_warehouse_path}")

    download_joke = BashOperator(task_id="random_joke", bash_command=f"curl -o {data_lake_path}/joke_{time_variable}.json https://official-joke-api.appspot.com/random_joke")

    # >> gives dependencies
    say_hello >> setup_folders >> download_joke