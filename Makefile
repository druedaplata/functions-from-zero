install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
test:
	python -m pytest -vv --cov=calcCLI --cov=mylib test_*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

format:
	black *.py mylib/*.py

deploy:
	echo "not implemented"

refactor: format lint

all: install lint test