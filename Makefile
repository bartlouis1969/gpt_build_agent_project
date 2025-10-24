# Makefile for common dev tasks

.PHONY: test lint type run clean freeze

test:
	pytest -q

lint:
	ruff check .

format:
	black .
	isort .

type:
	mypy .

run:
	uvicorn app.main:app --reload

freeze:
	pip freeze > requirements.txt

clean:
	rm -rf .pytest_cache __pycache__ */__pycache__ .mypy_cache .ruff_cache
