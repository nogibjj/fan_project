install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py **/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py **/*.py

test: 
	python -m pytest -vv test_*.py

refactor: format lint

all: install lint test 