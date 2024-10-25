FROM python:3.12-slim

WORKDIR /worker

RUN pip install aio-pika===9.4.3 pydantic==2.9.2 pandas==2.2.2 lasio===0.31 missingno===0.5.2 seaborn===0.13.2 plotly-express===0.4.1

COPY . .

CMD ["python3", "main.py"]
