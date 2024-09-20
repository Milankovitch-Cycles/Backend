FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8080

ENV TZ=America/Argentina/Buenos_Aires

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
