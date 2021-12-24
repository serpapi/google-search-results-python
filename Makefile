# Automate pip package development
#
# current version
version=$(shell grep version setup.py | cut -d"'" -f2)

.PHONY: build

all: clean install test test2

clean:
	find . -name '*.pyc' -delete
	find . -type d -name "__pycache__" -delete
	pip3 uninstall google_search_results

install:
	pip3 install -r requirements.txt

# Test with Python 3
test:
	pytest

# run example only 
#  and display output (-s)
example:
	pytest -s "tests/test_example.py::TestExample::test_async"

build_dep:
	pip3 install -U setuptools

# https://packaging.python.org/tutorials/packaging-projects/
build:
	python3 setup.py sdist

oobt: build
	pip3 install ./dist/google_search_results-$(version).tar.gz
	python3 oobt/oobt.py

check: oobt
	twine check dist/google_search_results-$(version).tar.gz

release: # check
	twine upload dist/google_search_results-$(version).tar.gz
