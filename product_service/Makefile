# 1. Определяем порт по умолчанию (если не передан в команде)
PORT ?= 8001

# 2. Формируем URL для этого сервиса. 
# Эту переменную может использовать Order Service, если он запускается в том же окружении.
export PRODUCT_SERVICE_URL=http://localhost:$(PORT)

# Команда для запуска сервиса
run:
	@echo "Запуск Product Service на порту $(PORT)..."
	@echo "URL для связи: $(PRODUCT_SERVICE_URL)"
	poetry run uvicorn src.app.main:app --host 0.0.0.0 --port $(PORT) --reload

# Вспомогательная команда для установки зависимостей (если нужно)
install:
	poetry install

# Очистка (необязательно, но полезно)
clean:
	rm -rf `find . -name __pycache__`
	rm -f .pytest_cache
