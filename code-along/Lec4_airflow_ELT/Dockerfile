FROM apache/airflow:latest-python3.9

# so python searches for setup/packages in specified folder
ENV PYTHONPATH=/opt/airflow
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt