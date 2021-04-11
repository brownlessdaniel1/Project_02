FROM python:3.8.5
ARG VERSION
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV VERSION=${VERSION}
ENTRYPOINT ["python3", "app.py"]
