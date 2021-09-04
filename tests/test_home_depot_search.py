import random
import unittest
import os
import pprint
from serpapi import HomeDepotSearch

class TestHomeDepotSearchApi(unittest.TestCase):

		def setUp(self):
				HomeDepotSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = HomeDepotSearch({"q": "chair"})
				data = search.get_dict()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["home_depot_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])
				self.assertTrue(len(data["products"]) > 5)
				self.assertIsNotNone(data["products"][0]["title"])

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_object(self):
				search = HomeDepotSearch({"q": "chair"})
				data = search.get_object()
				self.assertEqual(data.search_metadata.status, "Success")
				self.assertEqual(type(data.products), list)
				self.assertIsNotNone(data.products[0].title)
				self.assertIsNotNone(data.search_metadata.id)
				self.assertIsNotNone(data.search_metadata.home_depot_url)
				self.assertEqual(data.search_parameters.q, "chair")
				self.assertEqual(data.search_parameters.engine, "home_depot")
				self.assertGreater(data.search_information.total_results, 10)

if __name__ == '__main__':
		unittest.main()
