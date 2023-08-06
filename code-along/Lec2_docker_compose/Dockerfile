FROM python:3.11

WORKDIR /app

# copy all from current local directory where Dockerfile is stored into docker container working dir
COPY . .

# packages needed
RUN pip install plotly_express dash

# port
EXPOSE 8050

# run when spinning up the container from image [interpretor, file]
CMD ["python", "./src/main.py"]