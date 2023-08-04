FROM python:3.11

# host container
ADD main.py .

RUN pip install plotly_express dash

# run when spinning up the container from image
CMD ["python", "./main.py"]