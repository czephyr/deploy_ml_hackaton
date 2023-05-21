FROM python:3.9-slim
WORKDIR ~

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /app .

EXPOSE 8080
CMD ["streamlit", "run", "api/main.py", "--server.port", "8080"]
