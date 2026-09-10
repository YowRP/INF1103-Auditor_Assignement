FROM python:3.11-slim
WORKDIR /app
COPY Auditor.py /app/Auditor.py
CMD ["python", "Auditor.py"]