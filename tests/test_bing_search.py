import random
import unittest
import os
import pprint
from serpapi import BingSearch

class TestBingSearchApi(unittest.TestCase):

		def setUp(self):
				BingSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = BingSearch({"q": "Coffee", "location": "Austin,Texas"})
				data = search.get_json()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["bing_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])
				self.assertIsNotNone(data["organic_results"][0]["title"])
				# pp = pprint.PrettyPrinter(indent=2)
				# pp.pprint(data)

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_paginate(self):
				page_size = 20
				search = BingSearch({"q": "Coffee", "location": "Austin,Texas", "first": 10, "count": page_size})

				limit = 4
				pages = search.pagination(limit=limit)

				page_count = 0
				result_count = 0

				for page in pages:
					page_count += 1
					result_count += len(page["organic_results"])

				self.assertEqual(page_count, limit)

if __name__ == '__main__':
		unittest.main()
