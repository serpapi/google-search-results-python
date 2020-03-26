# current version

version=$(shell grep version setup.py | cut -d"'" -f2)

.PHONY: build

all: clean install test test2

clean:
	find . -name '*.pyc' -delete
	find . -type d -name "__pycache__" -delete

install:
	pip3 install -r requirements.txt

# Test with Python 3
test:
	pytest

# Test with python 2.7
test2:
	py.test-2.7

# run example only
example:
	pytest -s "tests/test_example.py::TestExample::test_async"

build_dep:
	pip3 install -U setuptools

# https://packaging.python.org/tutorials/packaging-projects/
build:
	python3 setup.py sdist

check: build
	twine check dist/google_search_results-$(version).tar.gz

release: check
	twine upload dist/google_search_results-$(version).tar.gz -u vikoky -p ${TWINE_PASSWORD}
