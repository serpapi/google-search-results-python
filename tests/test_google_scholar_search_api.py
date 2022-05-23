import random
import unittest
import os
import pprint
from serpapi import GoogleScholarSearch
   
class TestGoogleScholarSearch(unittest.TestCase):

		def setUp(self):
				GoogleScholarSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = GoogleScholarSearch({"q": "Coffee"})
				data = search.get_json()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["id"])
				self.assertIsNotNone(data["organic_results"][0]["title"])

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_paginate(self):
				page_size = 20
				search = GoogleScholarSearch({"q": "Coffee", "start": 10, "num": page_size})

				limit = 3
				pages = search.pagination(limit=limit)
				page_count = 0
				result_count = 0

				for page in pages:
						page_count += 1
						result_count += len(page["organic_results"])

				self.assertEqual(page_count, limit)

if __name__ == '__main__':
		unittest.main()
