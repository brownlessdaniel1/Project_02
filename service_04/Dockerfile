FROM python:3.8.5
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY test-db .
EXPOSE 5003
ENTRYPOINT ["python3", "app.py"]
