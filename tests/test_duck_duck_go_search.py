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

				for organic_result in data.get("organic_results", []):
						self.assertIsNotNone(organic_result.get("title"))

				# pp = pprint.PrettyPrinter(indent=2)
				# pp.pprint(data)
				self.assertTrue(len(data.keys()) > 3)

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_paginate_page_size(self):
				limit = 3

				params = {
					"q": "coffee",
				}

				titles = []

				search = DuckDuckGoSearch(params)
				pages = search.pagination(limit=limit)

				page_number = 0
				count = 0

				for page in pages:
					page_number += 1

					for organic_results in page.get("organic_results", []):
						count += 1
						title_index = 0

						for title in titles:
							title_index += 1

							if title == organic_results.get('title'):
								print("%d duplicated title: %s at index: %d" % (count, title, title_index))

						titles.append(organic_results['title'])

				self.assertEqual(page_number, limit, "Number of pages doesn't match.")


if __name__ == '__main__':
		unittest.main()
