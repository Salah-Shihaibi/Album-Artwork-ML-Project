FROM python:3

WORKDIR /app

ENV FLASK_APP=main.py

ENV FLASK_ENV=development

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "bash", "./start_flask.sh" ]
