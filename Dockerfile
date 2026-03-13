FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd --create-home appuser && chown -R appuser:appuser /app

USER appuser

COPY --chown=appuser:appuser . .

ENV FLASK_SECRET_KEY=${FLASK_SECRET_KEY:-changeme}
ENV FLASK_DEBUG=${FLASK_DEBUG:-false}
ENV PORT=5000
ENV LOG_LEVEL=INFO
ENV REDIS_URL=${REDIS_URL:-redis://redis:6379/0}

EXPOSE 5000

CMD ["python", "app.py"]
