FROM python:3.13-slim

WORKDIR /app

# Update OS packages
RUN apt-get update && apt-get upgrade -y && apt-get clean

COPY requirements.txt .

# Install latest secure dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
