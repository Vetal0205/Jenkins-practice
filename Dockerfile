FROM python:3.11.5-slim

WORKDIR /app


COPY test_note_book.py .
COPY requirements.txt .
RUN pip install -r requirements.txt


CMD ["python", "notebook.py"]
