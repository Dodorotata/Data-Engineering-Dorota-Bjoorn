# -------- traditioinal airflow code below (new way is TaskFlowAPI)-----------

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from pathlib import Path
import numpy as np

simulation_path = Path(__file__).parents[1] / "data" / "dice_simulations"


# simulate dice rolls
def _dice_rolls(number_rolls):  # _func convention for collable in python
    return list(np.random.randint(1, 7, size=number_rolls))


# pull data from xcom DB and append to txt file
def _save_dice_experiment(task_instance):
    simulation_data = task_instance.xcom_pull(task_ids=["roll_dice"])

    # validation code
    # ...

    with open(simulation_path / "dice_rolls.txt", "a") as file:
        file.write(f"Dice rolls {datetime.now()} \n")
        file.write(f"{simulation_data} \n\n")


 # scheduling according to Crontab syntax avery 30 min from 8 am -> first run 8:30, catchup=True backfills on missed historical scheduled tasks from start to now
with DAG(dag_id="dice_simulator", start_date=datetime(2023, 8, 8), schedule = "*/30 8 * * *", catchup=True):  
    setup_directories = BashOperator(
        task_id="setup_directories", bash_command=f"mkdir -p {simulation_path}"
    )

    dice_rolls = PythonOperator(
        task_id="roll_dice",
        python_callable=_dice_rolls,
        op_args=[10],  # op_args to pass in value for number_rolls to _dice_rolls
        do_xcom_push=True,  # push data to xcom DB (tmp storage between tasks, for small data amounts, could be further connected to a larger DB)
    )

    save_dice_experiment = PythonOperator(
        task_id="save_to_file",
        python_callable=_save_dice_experiment # no op_args
    )

    setup_directories >> dice_rolls >> save_dice_experiment


