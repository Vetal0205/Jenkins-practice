FROM python:3.11.5-slim

WORKDIR /app


COPY test_note_book.py .
RUN pip install -r requirements.txt


