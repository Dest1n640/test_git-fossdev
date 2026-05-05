.PHONY: create-structure install lint format build up down restart clean help

# Переменные
COMPOSE = docker-compose
SERVICES = order_service product_service discount_service

help:
	@echo "Управление проектом:"
	@echo "  make create-structure NAME=path  - Создать структуру нового сервиса"
	@echo "  make install                    - Установить зависимости для всех сервисов"
	@echo "  make lint                       - Проверить стиль кода и типы (ruff + mypy)"
	@echo "  make format                     - Исправить стиль кода (ruff)"
	@echo "  make build                      - Собрать Docker-образы"
	@echo "  make up                         - Запустить систему в Docker"
	@echo "  make down                       - Остановить и удалить контейнеры"
	@echo "  make restart                    - Пересобрать и перезапустить"
	@echo "  make clean                      - Удалить мусор и кеш"

# Твой исходный таргет
create-structure:
ifndef NAME
	$(error Надо указать имя папки: make create-structure NAME=my_project)
endif
	mkdir -p $(NAME)/src $(NAME)/tests $(NAME)/docs
	touch $(NAME)/README.md $(NAME)/setup.py $(NAME)/requirements.txt
	touch $(NAME)/docs/DOMAIN.md
	touch $(NAME)/src/.gitkeep $(NAME)/tests/.gitkeep
	@echo "Проект $(NAME) успешно создан"

# Автоматизация зависимостей (Poetry)
install:
	for dir in $(SERVICES); do \
		cd $$dir && poetry install && cd ..; \
	done

# Проверка качества кода
lint:
	poetry run ruff check .
	poetry run mypy .

format:
	poetry run ruff format .

# Docker команды
build:
	$(COMPOSE) build

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

restart: down build up

# Очистка (чтобы git был чистым, как просят в задании)
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .mypy_cache .ruff_cache .pytest_cache
	$(COMPOSE) down -v
