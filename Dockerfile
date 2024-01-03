FROM python:3.7-alpine

WORKDIR /app

ENV code_app app.python

ENV code_app_host 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "flask", "run"]

