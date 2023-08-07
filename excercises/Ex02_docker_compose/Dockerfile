FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install requests beautifulsoup4 

EXPOSE 8050

CMD ["python", "./src/main.py"]