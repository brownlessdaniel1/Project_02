FROM python:3.8.5
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5003
ENV DATABASE_URI $DATABASE_URI
ENTRYPOINT ["python3", "app.py"]
