import random
import unittest
import os
import pprint
from serpapi import YahooSearch

class TestYahooSearchApi(unittest.TestCase):

		def setUp(self):
				YahooSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = YahooSearch({"p": "Coffee"})
				data = search.get_json()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["yahoo_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])

				for organic_result in data.get("organic_results", []):
						self.assertIsNotNone(organic_result.get("title"))


		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_paginate(self):
				page_size = 7
				search = YahooSearch({"p": "Coffee", "b": page_size, "pz": page_size})

				limit = 4
				pages = search.pagination(limit=limit)

				titles = []
				page_number = 0

				for page in pages:
						organic_results_count = 0
						page_number += 1

						for organic_result in page.get("organic_results", []):
								organic_results_count += 1
								title_index = 0

								for id in titles:
										title_index += 1

										if id == organic_result.get("title"):
												print(f"{organic_results_count} duplicated title: {id} at index: {title_index}")

								titles.append(organic_result.get("title"))

						self.assertEqual(
								organic_results_count,
								page_size,
								f"page {page_number} does not contain {page_size} elements",
						)

				self.assertEqual(page_number, limit, "Number of pages doesn't match.")

if __name__ == '__main__':
		unittest.main()
