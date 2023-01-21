FROM python:latest

COPY . .

RUN pip install -r requirements.txt

WORKDIR /tests/

CMD ["pytest"]