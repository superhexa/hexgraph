FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1020

ENV PORT=1020

CMD ["python", "app.py"]
