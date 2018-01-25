FROM python:alpine

WORKDIR build

COPY requirements.txt .
RUN python3 -m pip install -U -r requirements.txt

WORKDIR /src
CMD python3 -m unittest && python3 app.py
