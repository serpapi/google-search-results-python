import random
import unittest
import os
import pprint
from serpapi import AppleAppStoreSearch

class TestAppleAppStoreSearch(unittest.TestCase):

		def setUp(self):
				AppleAppStoreSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = AppleAppStoreSearch({"term": "Coffee"})
				data = search.get_dict()
				self.assertEqual(data["search_metadata"]["status"], "Success")
				#self.assertIsNotNone(data["search_metadata"]["app_store_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])
				if "organic_results" in data:
					self.assertIsNotNone(data["organic_results"][1]["title"])
				pp = pprint.PrettyPrinter(indent=2)
				pp.pprint(data)
				print(data.keys())

if __name__ == '__main__':
		unittest.main()
