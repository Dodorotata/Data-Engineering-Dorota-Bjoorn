from airflow.decorators import dag, task_group, task
from datetime import datetime
from include.setup import setup_directories        # container has 1st level directory include containing file setup containing function setup_directories

#--- gå genom denna kod---------
from include.queue_time.extract import extract_queue_time
from include.queue_time.load import load_datalake


# create DAG (samma som with DAG(dag_id="dice_simulator", start_date=... fast annan syntax)
@dag(
    dag_id="queue_time_ELT",
    start_date=datetime(2023, 6, 8),
    schedule="*/5 * * * *",
    end_date=datetime(2023, 6, 11),
    catchup=False,
)
def queue_time_ELT():
    setup = setup_directories()
    extract_queue_time_ = extract_queue_time()
    load_queue_time = load_datalake()

    # dummy parallel task_group
    @task_group(group_id = "extract_airquality")
    def airquality():
        @task(task_id = "extract")
        def extract():
            return "temperature dummy"


    setup >> extract_queue_time_ >> load_queue_time

    setup >> airquality()

# register DAG
queue_time_ELT()