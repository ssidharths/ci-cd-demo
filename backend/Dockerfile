FROM python:3.8-slim

WORKDIR /app

# Copy requirements first (for better Docker caching)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
