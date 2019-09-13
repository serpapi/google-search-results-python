from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open('README.rst') as fp:
    README = fp.read()

setup(name='google_search_results',
      version='1.5.4',
      description='Scrape and search localized results from Google, Bing, Baidu at scale using SerpApi.com',
      url='https://github.com/serpapi/google-search-results-python',
      author='vikoky',
      author_email='victor@serpapi.com',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English',
        'Topic :: Utilities',
        ],
    python_requires='>=2.6, >=3.6',
    zip_safe=False,
    include_package_data=True,
    license="MIT",
    install_requires = ["requests"],
    packages=['lib'],
    keywords='scrape,serp,api,json,search,localized,rank,google,bing,baidu,scale,datamining,training,machine',
    long_description=README,
    long_description_content_type="text/x-rst",
)
