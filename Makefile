PYTHON_FILES := ids706_mini_project tests

install:
	pip install -r requirements.txt

format:
	black $(PYTHON_FILES)

lint:
	flake8 $(PYTHON_FILES)

test:
	pytest tests

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +

check-format:
	black --check $(PYTHON_FILES)

ci: lint test check-format
