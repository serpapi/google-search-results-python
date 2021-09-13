import random
import unittest
import os
import pprint
from serpapi import DuckDuckGoSearch

class TestDuckDuckGoSearch(unittest.TestCase):

		def setUp(self):
				DuckDuckGoSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = DuckDuckGoSearch({"q": "Coffee"})
				data = search.get_json()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["duckduckgo_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])
				if "organic_results" in data:
					self.assertIsNotNone(data["organic_results"][1]["title"])
				# pp = pprint.PrettyPrinter(indent=2)
				# pp.pprint(data)
				self.assertTrue(len(data.keys()) > 10)


		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_paginate(self):
			search = DuckDuckGoSearch({"q": "coffee",})
			pages = search.pagination(20, 60)
			page_count = 0
			result_count = 0
			for page in pages:
				page_count += 1
				result_count += len(page["organic_results"])
			self.assertEqual(page_count, 2)
			self.assertEqual(page_count, 40)

if __name__ == '__main__':
		unittest.main()
