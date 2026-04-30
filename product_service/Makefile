PORT ?= 8001

run:
	@echo "Запуск Product Service на порту $(PORT)..."
	poetry run uvicorn src.app.main:app --host 127.0.0.1 --port $(PORT) --reload

install:
	poetry install

clean:
	rm -rf `find . -name __pycache__`
	rm -f .pytest_cache
