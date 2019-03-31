# current version
version=`grep version setup.py | cut -d"'" -f2`

all: install test

install:
	pip3 install -r requirements.txt

# run test
test:
	pytest

# https://packaging.python.org/tutorials/packaging-projects/
release:
	pip3 install -U setuptools
	python setup.py sdist

publish:
	twine upload dist/google_search_results-$(version).tar.gz
