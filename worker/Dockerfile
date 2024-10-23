FROM python:3.12-slim

WORKDIR /worker

RUN pip install aio-pika===9.4.3 pydantic==2.9.2

COPY . .

CMD ["python3", "main.py"]
