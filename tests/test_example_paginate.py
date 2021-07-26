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
        "api_key": os.getenv("API_KEY")
      }
      # as proof of concept 
      #  urls collects
      urls = []
      # initialize a search
      search = GoogleSearch(params)
      # create a python generator
      pages = search.pagination(start, end)
      # fetch one search result per iteration 
      #  using a basic python for loop 
      #   which invokes python iterator under the hood.
      for page in pages:
        #print(f"Current page: {page['serpapi_pagination']['current']}")
        for news_result in page["news_results"]:
            #print(f"Title: {news_result['title']}\nLink: {news_result['link']}\n")
            urls.append(news_result['link'])
      # double check if things adds up.
      # total number pages expected
      #  the exact number if variable depending on the search engine backend
      self.assertEqual(len(urls), 20, "number of search results")
      self.assertEqual(len(set(urls)), len(urls), "duplicated elements detected")

    @unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
    def test_paginate_page_size(self):
      # to get 2 pages with each page contains 20 search results
      start = 0
      end = 80
      page_size = 20

      # use parameters in
      params = {
        "q": "coca cola",
        "tbm": "nws",
        "api_key": os.getenv("API_KEY"),
        "start": start,
        "end": end,
        "num": page_size
      }
      urls = []
      search = GoogleSearch(params)
      # parameter start,end,page_size will be used instead of pagination
      pages = search.pagination()
      page_count = 0
      count = 0
      for page in pages:
        page_count += 1
        # print(f"Current page: {page['serpapi_pagination']['current']}")
        for news_result in page["news_results"]:
            count += 1
            # print(f"{count} - title: {news_result['title']}")
            urls.append(news_result['link'])
            
      # check number of pages match
      self.assertEqual(page_count, 4)
      self.assertEqual(len(urls), end, "number of search results")
      self.assertEqual(len(set(urls)), end, "duplicated search results")
