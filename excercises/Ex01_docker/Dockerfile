# base imgage
FROM python:3.9

# defining working directory
WORKDIR /Exercise1

# packages needed
#RUN pip install matplotlib plotly_express pandas numpy dash sklearn prettytable

RUN pip install prettytable
RUN apt update && apt install -y nano cron

# layers added to base image
ADD ./src/ex1_0_setup.py .
ADD ./src/ex1_1_setup.py .
ADD ./src/dates.csv .
ADD ./src/installed_packages.sh .

RUN mkdir logs

# port
EXPOSE 8050

# run when spinning up the container from image [interpretor, file]
CMD ["bash", "installed_packages.sh"]
