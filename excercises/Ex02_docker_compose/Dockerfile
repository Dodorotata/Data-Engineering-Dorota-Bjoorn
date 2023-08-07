FROM python:3.11

WORKDIR /ex2

COPY . .

RUN pip install requests beautifulsoup4 

EXPOSE 8050

CMD ["python", "./src/all_to_scv.py"]