FROM python:3.9

WORKDIR /dash

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8050:8050

CMD ["bash", "./load_and_run.sh"]

# CMD ["python","./scripts/main.py","./scripts/dashboard.py"] does not work as third argument is interpreted as part of the second