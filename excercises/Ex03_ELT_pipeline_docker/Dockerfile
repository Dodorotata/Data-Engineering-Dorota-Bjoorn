FROM python:3.9

WORKDIR /dash

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8050:8050

#RUN ["crontab", "runmain.crontab"]

# can not run 2  programs from CMD command so listed in load_and_run.sh
CMD ["bash", "./load_and_run.sh"]