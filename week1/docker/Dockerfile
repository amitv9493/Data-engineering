FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2-binary

WORKDIR /app

COPY ingest-data.py ingest-data.py
COPY taxi_data.csv taxi_data.csv

ENTRYPOINT [ "python","ingest-data.py" ]