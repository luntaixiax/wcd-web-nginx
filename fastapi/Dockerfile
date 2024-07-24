FROM python:3.10-slim

ENV PORT=5000
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY run.sh run.sh
RUN chmod +x ./run.sh

EXPOSE ${PORT}