FROM python:3.11-slim

# ВАЖНО: версия 1.8.3
ENV POETRY_VERSION=1.8.3 \
  POETRY_VIRTUALENVS_CREATE=false \
  PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

# Копируем конфиг Poetry
COPY pyproject.toml /app/

# Устанавливаем зависимости. Теперь package-mode=false сработает.
RUN poetry install --no-interaction --no-ansi --no-root

# Копируем весь код (включая папку src)
COPY . /app

# Запуск по твоей структуре src/app/main.py
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
