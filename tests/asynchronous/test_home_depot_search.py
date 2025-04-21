import random
import unittest
import os
import pprint
from serpapi import AsyncHomeDepotSearch

class TestAsyncHomeDepotSearchApi(unittest.IsolatedAsyncioTestCase):

		def setUp(self):
				AsyncHomeDepotSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		async def test_get_json(self):
				search = AsyncHomeDepotSearch({"q": "chair"})
				data = await search.get_dict()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["home_depot_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])
				self.assertTrue(len(data["products"]) > 5)

				for product in data.get("products", []):
					self.assertIsNotNone(product["title"])

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		async def test_get_object(self):
				search = AsyncHomeDepotSearch({"q": "chair"})
				data = await search.get_object()
				self.assertEqual(data.search_metadata.status, "Success")
				self.assertEqual(type(data.products), list)
				self.assertIsNotNone(data.products[0].title)
				self.assertIsNotNone(data.search_metadata.id)
				self.assertIsNotNone(data.search_metadata.home_depot_url)
				self.assertEqual(data.search_parameters.q, "chair")
				self.assertEqual(data.search_parameters.engine, "home_depot")
				self.assertGreater(data.search_information.total_results, 10)

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		async def test_paginate_page_size(self):
			start = 24
			limit = 3

			# use parameters in
			params = {
				"q": "coffee",
				"start": start,
			}

			titles = []

			search = AsyncHomeDepotSearch(params)
			pages = search.pagination(limit=limit)

			page_number = 0
			count = 0

			async for page in pages:
				page_number += 1

				for product in page.get("products", []):
					count += 1
					i = 0

					for t in titles:
						i += 1

						if t == product.get('title'):
							print("%d duplicated title: %s at index: %d" % (count, t, i))

					titles.append(product['title'])

			self.assertEqual(page_number, limit, "Number of pages doesn't match.")

if __name__ == '__main__':
		unittest.main()
