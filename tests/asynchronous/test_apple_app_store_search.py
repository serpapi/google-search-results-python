import unittest
import os
import pprint
from serpapi import AsyncAppleAppStoreSearch

class TestAsyncAppleAppStoreSearch(unittest.IsolatedAsyncioTestCase):

		def setUp(self):
				AsyncAppleAppStoreSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		async def test_get_json(self):
				search = AsyncAppleAppStoreSearch({"term": "Coffee"})
				data = await search.get_dict()
				self.assertEqual(data["search_metadata"]["status"], "Success")
				#self.assertIsNotNone(data["search_metadata"]["app_store_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])
				if "organic_results" in data:
					self.assertIsNotNone(data["organic_results"][1]["title"])
				pp = pprint.PrettyPrinter(indent=2)
				pp.pprint(data)
				print(data.keys())

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		async def test_paginate(self):
				page_size = 20
				search = AsyncAppleAppStoreSearch({"term": "Coffee", "page": 0, "num": page_size})

				limit = 4
				pages = search.pagination(limit=limit)

				page_count = 0
				result_count = 0

				async for page in pages:
					page_count += 1
					result_count += len(page["organic_results"])

				self.assertEqual(page_count, limit)

if __name__ == '__main__':
		unittest.main()
