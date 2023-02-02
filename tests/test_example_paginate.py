import unittest
import os
from serpapi import GoogleSearch

# original code: https://replit.com/@DimitryZub1/Scrape-Google-News-with-Pagination-python-serpapi
class TestExamplePaginate(unittest.TestCase):
    
    @unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
    def test_paginate(self):
      # to get 2 pages
      limit = 2
      # basic search parameters
      params = {
        "q": "coca cola",
        "tbm": "nws",
        "api_key": os.getenv("API_KEY")
      }
      # as proof of concept 
      #  title collects
      title = []

      # initialize a search
      search = GoogleSearch(params)

      # create a python generator
      pages = search.pagination(limit=limit)
      # fetch one search result per iteration 
      #  using a basic python for loop 
      #   which invokes python iterator under the hood.

      page_count = 0

      for page in pages:
        page_count += 1
        #print(f"Current page: {page['serpapi_pagination']['current']}")
        for news_result in page["news_results"]:
            #print(f"Title: {news_result['title']}\nLink: {news_result['link']}\n")
            title.append(news_result['title'])

      # double check if things adds up.
      # total number pages expected
      #  the exact number if variable depending on the search engine backend
      self.assertEqual(page_count, limit)
      # self.assertEqual(len(title), 20, "number of search results")
      #self.assertEqual(len(set(title)), len(title), "duplicated elements detected")

    @unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
    def test_paginate_page_size(self):
      # to get 4 pages with each page contains 20 search results
      start = 0
      end = 80
      page_size = 20

      limit = (end - start) / page_size

      # use parameters in
      params = {
        "q": "coca cola",
        "tbm": "nws",
        "api_key": os.getenv("API_KEY"),
        "start": start,
        "end": end,
        "num": page_size
      }

      title = []

      search = GoogleSearch(params)

      # parameter limit will be used instead of pagination
      pages = search.pagination(limit=limit)

      page_count = 0
      count = 0

      for page in pages:
        page_count += 1
        # print(f"Current page: {page['serpapi_pagination']['current']}")
        for news_result in page["news_results"]:
            count += 1
            i = 0
            for t in title:
              i += 1
              if t == news_result['title']:
                print(("%d duplicated title: %s at index: %d" % (count, t, i)))
            #print(f"{count} - title: {news_result['title']}")
            title.append(news_result['title'])

      # check number of pages match
      self.assertEqual(page_count, limit, "Number of pages doesn't match.")
      # google randomly duplicated search result
      # self.assertEqual(len(set(title)), end, "duplicated search results")
