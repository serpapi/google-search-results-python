import random
import unittest
import os
import pprint
from serpapi import WalmartSearch


class TestWalmartSearchApi(unittest.TestCase):
		def setUp(self):
				WalmartSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = WalmartSearch({"query": "Coffee"})
				data = search.get_json()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["walmart_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])

				for organic_result in data.get("organic_results", []):
						self.assertIsNotNone(organic_result.get("title"))

				pp = pprint.PrettyPrinter(indent=2)
				pp.pprint(data)
				print(data.keys())

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_paginate(self):
				page_size = 50
				search = WalmartSearch({"query": "Coffee", "page": 1, "ps": page_size})

				limit = 4
				pages = search.pagination(limit=limit)

				product_ids = []
				page_number = 0

				for page in pages:
						organic_results_count = 0
						page_number += 1

						for organic_result in page.get("organic_results", []):
								organic_results_count += 1
								product_id_index = 0

								for id in product_ids:
										product_id_index += 1

										if id == organic_result.get("product_id"):
												print(f"{organic_results_count} duplicated product_id: {id} at index: {product_id_index}")

								product_ids.append(organic_result.get("product_id"))

				self.assertEqual(page_number, limit, "Number of pages doesn't match.")


if __name__ == "__main__":
		unittest.main()
