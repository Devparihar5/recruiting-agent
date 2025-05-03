FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--threads=4", "app:app"]
