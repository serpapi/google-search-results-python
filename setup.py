from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='google_search_results',
      version='1.2.2',
      description='this pip package is meant to scrape and parse Google results using SERP API. Feel free to fork this repository to add more backends.',
      url='https://github.com/serpapi/google-search-results-python',
      author='lf2225',
      author_email='lf2225@gmail.com',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        ],
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*',
    install_requires = ["requests"],
    packages=['lib'],
    long_description=open('README').read()
)
