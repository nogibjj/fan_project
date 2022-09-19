install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

refactor: format lint

all: install lint