FROM apache/airflow:latest-python3.9

# so python searches for setup/packages and paths in specified folder (/opt/airflow in docker corresponds to Lec4_airflow_ELT locally)
ENV PYTHONPATH=/opt/airflow
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt