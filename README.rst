===============================================
Google / Bing / Baidu Search Results in Python
===============================================

This Python package is meant to scrape and parse Google, Google Scholar, Bing, Baidu, Yandex, Yahoo, Ebay results using `SerpApi <https://serpapi.com>`_. 
The following services are provided:

* `Search API <https://serpapi.com/search-api>`_ 
* `Search Archive API <https://serpapi.com/search-archive-api>`_
* `Account API <https://serpapi.com/account-api>`_ 
* `Location API <https://serpapi.com/locations-api>`_

SerpApi provides a `script builder <https://serpapi.com/demo/>`_ to get you started quickly.


Installation
-------------

Compatible with Python 3.7+

.. code-block:: shell

    pip install google-search-results

`Link to the python package page <https://pypi.org/project/google-search-results>`_

Quick start
-------------

.. code-block:: python

    from serpapi import GoogleSearch
    search = GoogleSearch({"q": "coffee", "location": "Austin,Texas", "api_key": "secretKey"})
    result = search.get_dict()

This example runs a search about "coffee" using your secret api key.

The Serp API service (backend)

* searches on Google using the query: q = "coffee"
* parses the messy HTML responses
* return a standardizes JSON response

The GoogleSearch class

* Format the request
* Execute GET http request against Serp API service
* Parse JSON response into a dictionary

Et voila..

Alternatively, you can search:

- Bing using BingSearch class
- Baidu using BaiduSearch class
- Yahoo using YahooSearch class
- duckduckgo using DuckDuckGoSearch class
- Ebay using EbaySearch class
- Yandex using YandexSearch class
- HomeDepot using HomeDepotSearch class
- GoogleScholar using GoogleScholarSearch class
- Youtube using YoutubeSearch class
- Walmart using WalmartSearch
- Apple App Store using AppleAppStoreSearch class
- Naver using NaverSearch class

See the `playground to generate your code. <https://serpapi.com/playground>`_

`Documentation available here <https://github.com/serpapi/google-search-results-python/blob/master/README.md>`_
