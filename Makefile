all: install test

install:
	pip3 install -r requirements.txt

# https://packaging.python.org/tutorials/packaging-projects/
release:
	pip3 install -U setuptools
	python setup.py sdist

test:
	pytest

