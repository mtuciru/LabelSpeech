FROM python:3.8

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app/src
COPY src .

CMD [ "python", "main.py" ]
