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
		def test_get_json_paginate(self):
				search = GoogleScholarSearch({"q": "Coffee"})
				pages = search.pagination(0, 20, 10)
				urls = []
				for page in pages:
					if ('pagination' in page) and ('next' in page['pagination']):
						urls.append(page['pagination']['next'])
				self.assertEqual(len(urls), 2)
				self.assertTrue("start=10" in urls[0])
				print(urls[1])
				self.assertTrue("start=20" in urls[1])

if __name__ == '__main__':
		unittest.main()
