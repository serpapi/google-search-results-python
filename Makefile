all: install test

install:
	pip install -r requirements.txt
	pip install pytes
test:
	pytest

