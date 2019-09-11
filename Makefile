# current version

version=$(shell grep version setup.py | cut -d"'" -f2)

.PHONY: build

all: install test

install:
	pip3 install -r requirements.txt

# run test
test:
	pytest

# run example only
example:
	pytest -s "tests/test_example.py::TestExample::test_async"

build_dep:
	pip3 install -U setuptools
	pip install readme_renderer

readme:
	@head -n 50 README.md > SHORT_README.md
	@echo "\nFor more [README](https://github.com/serpapi/google-search-results-python/blob/master/README.md)" >> SHORT_README.md

# https://packaging.python.org/tutorials/packaging-projects/
build: readme
	python setup.py sdist

check: build
	twine check dist/google_search_results-$(version).tar.gz

release: check
	twine upload dist/google_search_results-$(version).tar.gz -u vikoky -p ${TWINE_PASSWORD}
