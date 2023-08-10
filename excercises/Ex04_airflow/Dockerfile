FROM apache/airflow:latest-python3.9
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# running Dockerfile as root => can change permissions (777 => all permissions for ownder group other )
RUN mkdir /opt/airflow/data
RUN chmod 777 /opt/airflow/data