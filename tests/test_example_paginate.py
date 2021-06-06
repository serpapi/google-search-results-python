import unittest
import os
from serpapi import GoogleSearch

# original code: https://replit.com/@DimitryZub1/Scrape-Google-News-with-Pagination-python-serpapi
class TestExamplePaginate(unittest.TestCase):
    @unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
    def test_paginate(self):
      # to get 2 pages
      start = 0
      end = 20
      # basic search parameters
      params = {
        "q": "coca cola",
        "tbm": "nws",
        "api_key": os.getenv("API_KEY"),
        "start": start,
        "end": end
      }
      # as proof of concept 
      #  urls collects
      urls = []
      # initialize a search
      search = GoogleSearch(params)
      # create a python generator
      pages = search.pagination()
      # fetch one search result per iteration 
      #  using a basic python for loop 
      #   which invokes python iterator under the hood.
      for page in pages:
        print(f"Current page: {page['serpapi_pagination']['current']}")
        for news_result in page["news_results"]:
            print(f"Title: {news_result['title']}\nLink: {news_result['link']}\n")
            urls.append(news_result['link'])
      # double check if things adds up.
      # total number pages expected
      #  the exact number if variable depending on the search engine backend
      self.assertGreater(len(urls), 200)
