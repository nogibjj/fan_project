install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	sudo apt-get install -y docker.io
	sudo service docker start
	sudo chmod 666 /var/run/docker.sock
format:	
	black *.py **/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py **/*.py

test: 
	python -m pytest -vv test_*.py

refactor: format lint

all: install format lint test 