# Google Search Results in Python

[![Package](https://badge.fury.io/py/google-search-results.svg)](https://badge.fury.io/py/google-search-results)
[![Build](https://github.com/serpapi/google-search-results-python/actions/workflows/python-package.yml/badge.svg)](https://github.com/serpapi/google-search-results-python/actions/workflows/python-package.yml)


## About 

[`google-search-results`](https://pypi.org/project/google-search-results) is a MIT-licensed [Python](https://www.python.org/) package that meant to [scrape](https://en.wikipedia.org/wiki/Web_scraping) search results from Google, Bing, Baidu, Yahoo and [10+ more search engines](#supported-engines) with a [SerpApi](https://serpapi.com) backend. SerpApi provides a [Playground](https://serpapi.com/playground) to get you started quickly by testing API interactively.

Find SerpApi documentation at: https://serpapi.com/search-api

Find SerpApi PyPi package at: https://pypi.org/project/google-search-results

<details>
<summary>Table of Contents</summary>

- [About](#about) 
- [Installation](#installation---python-37) 
- [Quick Start](#quick-start) 
- [Search Google Images](#search-google-images) 
- [Search Google Images with Pagination](#search-google-images-with-pagination) 
- [Supported Engines](#supported-engines) 
- [Google Search API Capability](#google-search-api-capability) 
- [How to set SerpApi key](#how-to-set-serpapi-key) 
- [Example by Specification](#example-by-specification) 
- [Extra APIs](#extra-apis)
- [Generic search with SerpApiClient](#generic-search-with-serpapiclient)
- [Google Search By Location](#google-search-by-location)
- [Batch Asynchronous Searches](#batch-asynchronous-searches)
- [Python object as a result](#python-object-as-a-result)
- [Pagination using iterator](#pagination-using-iterator)
- [Error management](#error-management)
- [Changelog](#change-log)
</details>

## Installation - Python 3.7+

```bash
pip install google-search-results
```

## Quick Start

[Open example on Replit](https://replit.com/@serpapi/google-search-results-quick-start#main.py) (online IDE).

The following example runs a search for `"coffee"` using your secret API key which you can find at [SerpApi Dashboard](https://serpapi.com/manage-api-key) page.

```python
from serpapi import GoogleSearch

search = GoogleSearch({
    "q": "coffee", 
    "location": "Austin,Texas",
    "api_key": "<your-serpapi-api-key>"
})

result = search.get_dict()
```

How SerpApi backend works:
- Searches Google using the search: `q` = `"coffee"`
- Parses the messy HTML responses.
- Returns a standardized JSON response. 

The `GoogleSearch()` class:
- Formats the request.
- Executes a `GET` HTTP request against SerpApi service.
- Parses the JSON response into a dictionary via [`get_dict()`](https://github.com/serpapi/google-search-results-python/blob/56447f2ac39f202fa663233c87fa7c7b9ca1e6b2/serpapi/serp_api_client.py#L98) function.

## Search Google Images

This code prints all the image links, and downloads the images if you un-comment the line with [`wget`](https://www.gnu.org/software/wget/) (Linux/OS X tool to download files).

This tutorial covers more ground on this topic at [serpapi/showcase-serpapi-tensorflow-keras-image-training](https://github.com/serpapi/showcase-serpapi-tensorflow-keras-image-training).

```python
from serpapi import GoogleSearch

search = GoogleSearch({"q": "coffe", "tbm": "isch"})

for image_result in search.get_dict()['images_results']:
    link = image_result["original"]

    try:
        print("link: " + link)
        # wget.download(link, '.')
    except:
        pass
```

## Search Google Images with Pagination

[Open example on Replit](https://replit.com/@serpapi/google-search-results-google-images-pagination-example#main.py) (online IDE).

```python
from serpapi import GoogleSearch

params = {
    "engine": "google",                  # parsing engine
    "q": "coffee",                       # search query
    "tbm": "isch",                       # image results
    "num": "100",                        # number of images per page
    "ijn": 0,                            # page number: 0 -> first page, 1 -> second...
    "api_key": "<your serpapi api key>"  # your serpapi api key
    # other query parameters: hl (lang), gl (country), etc  
}

search = GoogleSearch(params)            # where data extraction happens

image_results = []

while True:
    results = search.get_dict()          # JSON -> Python dictionary

    # checks for "Google hasn't returned any results for this query."
    if "error" not in results:
        for image in results["images_results"]:
            if image["original"] not in image_results:
                image_results.append(image["original"])
        
        # update to the next page
        params["ijn"] += 1
    else:
        break
        print(results["error"])

print(image_results)
```
<h3 align="center">💡<a href="https://github.com/serpapi/google-search-results-python/tree/master/examples/pagination">Pagination examples for currently supported APIs</a>💡</h4>

## Supported Engines

| Engine                                                                       | Class name              |
|------------------------------------------------------------------------------|-------------------------|
| [Google Search Engine](https://serpapi.com/search-api)                       | `GoogleSearch()`        |
| [Google Maps](https://serpapi.com/google-jobs-api)                           | `GoogleSearch()`        |
| [Google Jobs](https://serpapi.com/google-jobs-api)                           | `GoogleSearch()`        |
| [Google Trends](https://serpapi.com/google-trends-api)                       | `GoogleSearch()`        |
| [Google Autocomplete](https://serpapi.com/google-autocomplete-api)           | `GoogleScholarSearch()` |
| [Google Related Questions](https://serpapi.com/google-related-questions-api) | `GoogleScholarSearch()` |
| [Google Scholar](https://serpapi.com/google-scholar-api)                     | `GoogleScholarSearch()` |
| [Google Play Store](https://serpapi.com/google-play-api)                     | `GoogleSearch()`        |
| [Google Product](https://serpapi.com/google-product-api)                     | `GoogleSearch()`        |
| [Google Immersive Product](https://serpapi.com/google-immersive-product-api) | `GoogleSearch()`        |
| [Google Reverse Image](https://serpapi.com/google-reverse-image)             | `GoogleSearch()`        |
| [Google Events](https://serpapi.com/google-events-api)                       | `GoogleSearch()`        |
| [Google Local Services](https://serpapi.com/google-local-services-api)       | `GoogleSearch()`        |
| [Bing](https://serpapi.com/bing-search-api)                                  | `BingSearch()`          |
| [Baidu](https://serpapi.com/baidu-search-api)                                | `BaiduSearch()`         |
| [DuckDuckGo](https://serpapi.com/duckduckgo-search-api)                      | `DuckDuckGoSearch()`    |
| [Yahoo](https://serpapi.com/yahoo-search-api)                                | `YahooSearch()`         |
| [Yandex](https://serpapi.com/yandex-search-api)                              | `YandexSearch()`        |
| [eBay](https://serpapi.com/ebay-search-api)                                  | `EbaySearch()`          |
| [Youtube](https://serpapi.com/youtube-search-api)                            | `YoutubeSearch()`       |
| [Walmart](https://serpapi.com/walmart-search-api)                            | `WalmartSearch()`       |
| [HomeDepot](https://serpapi.com/home-depot-search-api)                       | `HomeDepotSearch()`     |
| [Apple App Store](https://serpapi.com/apple-app-store)                       | `AppleAppStoreSearch()` |
| [Naver](https://serpapi.com/naver-search-api)                                | `NaverSearch()`         |
| [Yelp](https://serpapi.com/yelp-search-api)                                  | `YelpSearch()`          |


## Google Search API Capability

```python
params = {
    "api_key": "asdewqe1231241asm",              # Your SerpApi API key.                                                                             
    "q": "coffee",                               # Search query.                                                                                     
    "google_domain": "google.com",               # Google domain to use.                                                                             
    "location": "Austin, Texas, United States",  # Location requested for the search.                                                                
    "uule": "w+CAIQICINVW5pdGVkIFN0YXRlcw",      # Google encoded location you want to use for the search.                                           
    "ludocid": "CID ID",                         # ID (CID) of the Google My Business listing you want to scrape.
    "lsig": "AB86z5W5r155sIcs3jqfYkm9Y8Fp",      # Force the knowledge graph map view to show up.
    "device": "desktop|mobile|tablet",           # Device used when making a search.                                                                 
    "hl": "en",                                  # Language of the search.                                                                           
    "gl": "gl",                                  # Country of the search.                                                                            
    "lr": "lang_en|lang_fr",                     # One or multiple languages to limit the search to.                                                 
    "safe": "active|off",                        # Level of filtering for adult content.                                                             
    "nfpr": "1|0",                               # Exclusion of results from an auto-corrected query that is spelled wrong.                          
    "num": "100",                                # Number of results per page.                                                                       
    "start": "20",                               # Pagination offset.                                                                                
    "ijn":"1",                                   # Page number for Google Images.                                                                    
    "tbm": "nws|isch|shop",                      # Type of search: news, images, shopping.                                                         
    "tbs": "custom to be search criteria",       # Advanced search for patents, dates, news, videos, images, apps, or text contents                  
    "async": True|False,                         # Allow async request.
    "no_cache": True|False                       # Force SerpApi to fetch the Google results even if a cached version is already present             
}                                                                    

search = GoogleSearch(params)                  # Define the search.                                                                                
search.params_dict["location"] = "Portland"    # Override an existing parameter.                                                                   
search.get_html()                              # Search format return as raw html (parse results).                                                 
search.get_dict()                              # Search format return as Python dictionary.                                                        
search.get_json()                              # Search format return as JSON using json package.
search.get_object()                            # Search format return as dynamic Python object.                                                    
```

## How to set SerpApi key

The SerpApi `api_key` can be set globally:

```python
GoogleSearch.SERP_API_KEY = "<your-serpapi-api-key>"
```

The SerpApi `api_key` can be provided for each search:

```python
query = GoogleSearch({"q": "coffee", "api_key": "<your-serpapi-api-key>"})
```

Using [Python system operating interface `os`](https://docs.python.org/3/library/os.html):

```python
import os 
query = GoogleSearch({"q": "coffee", "api_key": os.getenv("<your-serpapi-api-key>")})
```

## Example by Specification

We love open source, continuous integration and [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) (TDD). We are using [RSpec](http://rspec.info/) to test [our infrastructure around the clock](https://travis-ci.org/serpapi/google-search-results-python) to achieve the best [Quality of Service](https://en.wikipedia.org/wiki/Quality_of_service) (QoS).
 
The directory `test/` includes specification/examples.

Set your API key:

```bash
export API_KEY="<your-serpapi-api-key>"
```

Run test:

```python
make test
```

## Extra APIs

### [Location API](https://serpapi.com/locations-api)

```python
from serpapi import GoogleSearch

search = GoogleSearch({})
location_list = search.get_location("Austin", 3)
print(location_list)
```

This prints the first 3 locations matching Austin (Texas, Texas, Rochester):

```python
[
   {
      "id":"585069bdee19ad271e9bc072",
      "google_id":200635,
      "google_parent_id":21176,
      "name":"Austin, TX",
      "canonical_name":"Austin,TX,Texas,United States",
      "country_code":"US",
      "target_type":"DMA Region",
      "reach":5560000,
      "gps":[
         -97.7430608,
         30.267153
      ],
      "keys":[
         "austin",
         "tx",
         "texas",
         "united",
         "states"
      ]
   }, ... 2 other locations
]
```

### [Search Archive API](https://serpapi.com/search-archive-api)

The search results are stored in a temporary cache. The previous search can be retrieved from the cache for free up to 31 days after the search has been completed.

```python
from serpapi import GoogleSearch

search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
search_result = search.get_dictionary()
assert search_result.get("error") == None
search_id = search_result.get("search_metadata").get("id")
print(search_id)
```

Now let's retrieve the previous search from the archive which prints the search result from the archive.

```python
archived_search_result = GoogleSearch({}).get_search_archive(search_id, 'json')
print(archived_search_result.get("search_metadata").get("id"))
```

### [Account API](https://serpapi.com/account-api)

This prints your account information: 

```python
from serpapi import GoogleSearch

search = GoogleSearch({})
account = search.get_account()
```

```json
{
   "account_id":"account-id",
   "api_key":"api-key",
   "account_email":"email",
   "plan_id":"free",
   "plan_name":"Free Plan",
   "searches_per_month":100,
   "plan_searches_left":0,
   "extra_credits":100,
   "total_searches_left":0,
   "this_month_usage":0,
   "this_hour_searches":0,
   "last_hour_searches":0,
   "account_rate_limit_per_hour":200000
}
```

## Generic search with SerpApiClient

This class enables interaction with any search engine supported by SerpApi.

```python
from serpapi import SerpApiClient

query = {"q": "Coffee", "location": "Austin,Texas", "engine": "google"}
search = SerpApiClient(query)
data = search.get_dict()
print(data)
```

## Google Search By Location

With SerpApi, we can build a Google search from anywhere in the world.
This code looks for the best coffee shop for the given cities.

```python
from serpapi import GoogleSearch

for city in ["new york", "paris", "berlin"]:
  location = GoogleSearch({}).get_location(city, 1)[0]["canonical_name"]

  search = GoogleSearch({
      "q": "best coffee shop",   # search search
      "location": location,
      "num": 1,
      "start": 0
  })

  data = search.get_dict()
  top_result = data["organic_results"][0]["title"]
```

## Batch Asynchronous Searches

We offer two ways to boost your searches thanks to the `async` parameter.

- Blocking: `async=false` - more compute intensive because the search needs to maintain many connections. (default) 
- Non-blocking: `async=true` - the way to go for large batches of queries (recommended)

This code shows how to run searches asynchronously:

```python
import os                         # Operating system
import re                         # regular expression library
from queue import Queue           # safe queue (named Queue in python2)
import time                       # Time utility
from serpapi import GoogleSearch  # SerpApi search

search_queue = Queue()            # store searches

# SerpApi search
search = GoogleSearch({
    "location": "Austin,Texas",
    "async": True,
    "api_key": os.getenv("API_KEY")
})

# loop through a list of companies
for company in ['amd', 'nvidia', 'intel']:
    print("execute async search: q = " + company)

    search.params_dict["q"] = company
    result = search.get_dict()

    if "error" in result:
        print("oops error: ", result["error"])
        continue

    print("add search to the queue where id: ", result['search_metadata'])

    # add search to the search_queue
    search_queue.put(result)

print("wait until all search statuses are cached or success")

# Create regular search
while not search_queue.empty():
    result = search_queue.get()
    search_id = result['search_metadata']['id']

    # retrieve search from the archive - blocker
    print(search_id + ": get search from archive")

    search_archived = search.get_search_archive(search_id)

    print(search_id + ": status = " +
          search_archived['search_metadata']['status'])

    # check status
    if re.search('Cached|Success',
                 search_archived['search_metadata']['status']):

        print(search_id + ": search done with q = " +
              search_archived['search_parameters']['q'])
    else:
        # requeue search_queue
        print(search_id + ": requeue search")
        search_queue.put(result)

        # wait 1s
        time.sleep(1)

print('all searches completed')
```

The search parameters must have `{async: True}`. This indicates that the client shouldn't wait for the search to be completed.
The current thread that executes the search is now non-blocking, which allows it to execute thousands of searches in seconds. The SerpApi backend will do the processing work.

The actual search result is deferred to a later call from the search archive using `get_search_archive(search_id)`.
In this example the non-blocking searches are persisted in a queue: `search_queue`.
A loop through the `search_queue` allows it to fetch individual search results.

This process can easily be multithreaded to allow a large number of concurrent search requests.
To keep things simple, this example only explores search results one at a time (single threaded).

[See example.](https://github.com/serpapi/google-search-results-python/blob/master/tests/test_example.py)

## Python object as a result

The search results can be automatically wrapped in dynamically generated Python object. This solution offers a more dynamic, fully [Oriented Object Programming](https://en.wikipedia.org/wiki/Object-oriented_programming) approach over the regular Dictionary / JSON data structure.

```python
from serpapi import GoogleSearch

search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
r = search.get_object()

assert type(r.organic_results), list
assert r.organic_results[0].title
assert r.search_metadata.id
assert r.search_metadata.google_url
assert r.search_parameters.q, "Coffee"
assert r.search_parameters.engine, "google"
```

## Pagination using iterator

[Open on Replit](https://replit.com/@serpapi/google-search-results-pagination-using-iterator-example?v=1) (online IDE).

```python
from serpapi import GoogleSearch

# parameters to get 2 pages
start = 0
end = 20
page_size = 10

parameter = {
  "q": "coca cola",                              # search query
  "tbm": "nws",                                  # news tab
  "api_key": "<your-serpapi-api-key>",           # serpapi api key
  "start": start,                                # optional pagination parameter. Can take argument directly
  "end": end,                                    # explicit parameter to pagination stop at 2nd page.
  "num": page_size                               # number of results per page
}

search = GoogleSearch(parameter)                 # initialize a search

urls = []                                        # urls collects

pages = search.pagination()                      # create a python generator using parameter
pages = search.pagination(start, end, page_size) # or set custom parameter

# fetch one search result per iteration 
# using a basic python for loop which invokes python iterator under the hood
for page in pages:
  print(f"Current page: {page['serpapi_pagination']['current']}")
  for news_result in page["news_results"]:
    print(f"Title: {news_result['title']}\nLink: {news_result['link']}\n")
    urls.append(news_result['link'])
  
# check if the total number pages is as expected
# note: the exact number if variable depending on the search engine backend
if len(urls) == (end - start):
  print("all search results count match!")
if len(urls) == len(set(urls)):
  print("all search results are unique!")
```

This example fetches links with pagination. [Test pagination file](https://github.com/serpapi/google-search-results-python/blob/master/tests/test_example_paginate.py).

## Error management

SerpApi keeps error management simple:

- backend service error or search fail.
- client error.

If it's a backend error, a simple error message is returned as string in the server response.

```python
from serpapi import GoogleSearch

search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas", "api_key": "<your-serpapi-api-key>"})
data = search.get_json()
assert data["error"] == None
```

In some cases, there are more details available in the data object. If it's a client error, then a `SerpApiClientException` is raised.

## Change log

2021-12-22 @ 2.4.1
 - add more search engine 
   - youtube
   - walmart
   - apple_app_store
   - naver 
 - raise SerpApiClientException instead of raw string in order to follow Python guideline 3.5+
 - add more unit error tests for serp_api_client

2021-07-26 @ 2.4.0
 - add page size support using num parameter
 - add youtube search engine

2021-06-05 @ 2.3.0
 - add pagination support

2021-04-28 @ 2.2.0
 - add get_response method to provide raw requests.Response object

2021-04-04 @ 2.1.0
 - Add home depot search engine
 - get_object() returns dynamic Python object
 
2020-10-26 @ 2.0.0
 - Reduce class name to <engine>Search
 - Add get_raw_json

2020-06-30 @ 1.8.3
 - simplify import
 - improve package for python 3.5+
 - add support for python 3.5 and 3.6

2020-03-25 @ 1.8
 - add support for Yandex, Yahoo, Ebay
 - clean-up test

2019-11-10 @ 1.7.1
 - increase engine parameter priority over engine value set in the class

2019-09-12 @ 1.7
 - Change  namespace "from lib." instead: "from serpapi import GoogleSearch"
 - Support for Bing and Baidu

2019-06-25 @ 1.6
 - New search engine supported: Baidu and Bing