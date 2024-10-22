FROM python:3.12-slim

WORKDIR /app/api

COPY requirements.txt .

RUN pip install -r ./requirements.txt

RUN mkdir db
COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
