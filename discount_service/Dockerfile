FROM python:3.11-slim

# Установка переменных окружения
ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  POETRY_VERSION=1.7.0 \
  POETRY_VIRTUALENVS_CREATE=false

# Установка системных зависимостей и Poetry
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

# Копируем только файлы зависимостей для кеширования слоев Docker
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем зависимости
RUN poetry install --no-interaction --no-ansi --no-root

# Копируем остальной код
COPY . /app

# Запускаем Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
