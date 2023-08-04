# base imgage
FROM python:3.11

# layers added to base image
ADD main.py .

# packages needed
RUN pip install plotly_express dash

# port
EXPOSE 8050

# run when spinning up the container from image [interpretor, file]
CMD ["python", "./main.py"]