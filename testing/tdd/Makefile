create-structure:
	mkdir src
	mkdir tests
	mkdir docs
	touch README.md
	touch setup.py
	touch requirements.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep
	touch tests/.gitkeep

# install-venv:
# 	python3.11 -m venv .venv 

install-dep:
	pip install -r requirements.txt

install:
	pip install -e .

test-pytest:
	python3 -m pytest 

test: install-venv install-dep install test-pytest
