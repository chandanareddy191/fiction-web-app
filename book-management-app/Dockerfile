FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=run.py

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]