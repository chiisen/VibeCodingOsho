FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_SECRET_KEY=${FLASK_SECRET_KEY:-changeme}
ENV FLASK_DEBUG=${FLASK_DEBUG:-false}
ENV PORT=5000
ENV LOG_LEVEL=INFO

EXPOSE 5000

CMD ["python", "app.py"]
