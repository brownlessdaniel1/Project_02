FROM python:3.8.5
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
ENTRYPOINT ["python3", "app.py"]
