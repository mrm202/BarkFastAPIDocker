FROM python:3.8-slim

WORKDIR /app
COPY ./main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt
RUN apt-get update && \
	apt-get install -y git && \
	pip install --no-cache-dir -r requirements.txt && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

#PORT
EXPOSE 8005
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8005
