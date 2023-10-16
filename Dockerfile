FROM python:3.11.5-slim

WORKDIR /app

COPY notebook.py .
COPY notebook.py .
RUN pip install -r requirements.txt

ENV NAME World


CMD ["python", "./notebook.py"]


# Define environment variable
