import random
import unittest
import os
import pprint
from serpapi import AsyncGoogleScholarSearch
   
class TestAsyncGoogleScholarSearch(unittest.TestCase):

		def setUp(self):
				AsyncGoogleScholarSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		async def test_get_json(self):
				search = AsyncGoogleScholarSearch({"q": "Coffee"})
				data = await search.get_json()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["id"])
				self.assertIsNotNone(data["organic_results"][0]["title"])

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		async def test_paginate(self):
				page_size = 20
				search = AsyncGoogleScholarSearch({"q": "Coffee", "start": 10, "num": page_size})

				limit = 3
				pages = search.pagination(limit=limit)
				page_count = 0
				result_count = 0

				async for page in pages:
						page_count += 1
						result_count += len(page["organic_results"])

				self.assertEqual(page_count, limit)

if __name__ == '__main__':
		unittest.main()
