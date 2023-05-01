# Automate pip package development
#
# current version
version=$(shell grep version setup.py | cut -d"'" -f2)

.PHONY: build

all: clean install lint test

clean:
	find . -name '*.pyc' -delete
	find . -type d -name "__pycache__" -delete
	pip3 uninstall google_search_results

create_env:
	python -m venv .env
	source .env/bin/activate

install:
	python3 -m pip install --upgrade pip
	if [ -f requirements.txt ]; then pip3 install -r requirements.txt; fi

lint: build_dep
	# stop the build if there are Python syntax errors or undefined names
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Test with Python 3
test: build_dep
	pytest --workers auto --tests-per-worker auto

# run example only 
#  and display output (-s)
example:
	pytest -s "tests/test_example.py::TestExample::test_async"

build_dep:
	pip3 install -U setuptools pytest py pytest-parallel flake8 twine

# https://packaging.python.org/tutorials/packaging-projects/
build: build_dep
	python3 setup.py sdist

oobt: build
	pip3 install ./dist/google_search_results-$(version).tar.gz
	python3 oobt/oobt.py

check: oobt
	twine check dist/google_search_results-$(version).tar.gz

release: # check
	twine upload dist/google_search_results-$(version).tar.gz
