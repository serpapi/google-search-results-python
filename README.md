# Google Search Results in Python

[![Build Status](https://travis-ci.org/serpapi/google-search-results-python.svg?branch=master)](https://travis-ci.org/serpapi/google-search-results-python)

This Python package is meant to scrape and parse Google results using [SERP API](https://serpapi.com). 
Feel free to fork this repository to add more backends.

## Simple Example
```python
from lib.google_search_results import GoogleSearchResults
query = GoogleSearchResults({"q": "coffee", "location": "Austin,Texas"})
json_results = query.get_json()
```

## Set SERP API key

```python
GoogleSearchResults.SERP_API_KEY = "Your Private Key"
```
Or
```python
query = GoogleSearchResults({"q": "coffee", "serp_api_key": "Your Private Key"})
```

## Example with all params and all outputs

```python
query_params = {
  "q": "query",
  "google_domain": "Google Domain",
  "location": "Location Requested",
  "device": device,
  "hl": "Google UI Language",
  "gl": "Google Country",
  "safe": "Safe Search Flag",
  "num": "Number of Results",
  "start": "Pagination Offset",
  "serp_api_key": "Your SERP API Key"
}

query = GoogleSearchResults[query_params]
query.params_dict["location"] = "Portland"

html_results = query.get_html()
json_results = query.get_json()
```

## Example of Python Dictionary Output (GoogleSearchResults#get_dictionary)

```python
dictionary_results = query.get_dictionary()
```
