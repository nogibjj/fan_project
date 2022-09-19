install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py **/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py **/*.py

refactor: format lint

all: install lint