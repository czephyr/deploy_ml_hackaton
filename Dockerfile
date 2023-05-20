FROM python:3.9-slim
WORKDIR ~
COPY /app .

EXPOSE 8080

RUN pip install --upgrade pip
RUN pip install pipenv

RUN pipenv install --deploy --ignore-pipfile

CMD ["pipenv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]
