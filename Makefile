install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
test:
	python -m pytest -vv --cov=wikiphrases --cov=nlplogic test_corenlp.py

lint:
	pylint --disable=R,C *.py 
format:
	black *.py

deploy:
	echo "not implemented"

refactor: format lint

all: install lint test