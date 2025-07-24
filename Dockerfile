FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
