all: lint test clean

lint:
	black .
	isort . --check
	pylint ./aoc2023 ./tests

test:
	pytest tests/ --cov=aoc2023 --cov-report=term-missing --cov-fail-under=100

clean:
	find . -name "__pycache__" -type d | xargs rm -rf
	find . -name ".pytest_cache" -type d | xargs rm -rf