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

build: 
	docker build -t split-money .

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 844619079882.dkr.ecr.us-east-1.amazonaws.com
	docker build -t sm .
	docker tag sm:latest 844619079882.dkr.ecr.us-east-1.amazonaws.com/sm:latest
	docker push 844619079882.dkr.ecr.us-east-1.amazonaws.com/sm:latest

run:
	docker run -e MYSQL_HOST=$(MYSQL_HOST) \
        -e MYSQL_USER=$(MYSQL_USER) \
        -e MYSQL_PWD=$(MYSQL_PWD) \
        -e MYSQL_DATABASE=$(MYSQL_DATABASE) \
		-p 8000:8000 \
        split-money 

all: install format lint test refactor