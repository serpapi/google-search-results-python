all: install test

install:
	pip install -r requirements.txt

test:
	pytest

