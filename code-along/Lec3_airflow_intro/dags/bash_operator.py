from airflow.operators.bash import BashOperator  # to have autofill etc
from airflow import DAG
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv  # for api key
import os  # for api key

load_dotenv()  # load info from .env
API_NINJA_KEY = os.environ.get(
    "API_NINJA"
)  # varable holding api key relevant for norris_joke


data_lake_path = Path(__file__).parents[1] / "data" / "datalake"
data_warehouse_path = Path(__file__).parents[1] / "data" / "data_warehouse"
# .as_posix() not needed since script wiill be run in docker container which is Linux (will not work outside though)

time_variable = "$(date +%y%m%d_%H%M%S)"

with DAG(dag_id="joke_DAG", start_date=datetime(2023, 8, 8)):
    say_hello = BashOperator(
        task_id="say_hello", bash_command="echo 'hej hej jokeing time'"
    )

    setup_folders = BashOperator(
        task_id="setup_folders",
        bash_command=f"mkdir -p {data_lake_path} {data_warehouse_path}",
    )

    download_joke = BashOperator(
        task_id="random_joke",
        bash_command=f"curl -o {data_lake_path}/joke_{time_variable}.json https://official-joke-api.appspot.com/random_joke",
    )

    download_norris_joke = BashOperator(
        task_id="chuck_norris_joke",
        bash_command=f"curl -H 'X-Api-Key: {API_NINJA_KEY}' -o {data_lake_path}/norris_{time_variable}.json https://api.api-ninjas.com/v1/chucknorris",
    )

    notify_number_files = BashOperator(
        task_id="notify_number_files",
        bash_command=f"echo $(ls {data_lake_path} | wc -l) jokes downloaded",       #coud be e-mail notification or other
    )

    # >> gives dependencies
    (
        say_hello
        >> setup_folders
        >> download_joke
        >> download_norris_joke
        >> notify_number_files
    )
