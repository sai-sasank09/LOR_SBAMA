FROM python:3.11-alpine

WORKDIR /LOR-PORTAL

COPY app app
COPY documents documents
COPY instance instance
COPY sample sample
COPY .env .env
COPY db_init.py db_init.py
COPY requirements.txt requirements.txt
COPY run.py run.py

RUN pip install -r requirements.txt

CMD python run.py