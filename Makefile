all: install test

install:
	pip install -r requirements.txt

# https://packaging.python.org/tutorials/packaging-projects/
package:
	pip install -U setuptools
	python setup.py sdist

test:
	pytest

