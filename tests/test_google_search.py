import random
import unittest
import os
import pprint
import requests
from serpapi import GoogleSearch

class TestSearchApi(unittest.TestCase):

		def setUp(self):
				GoogleSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_paginate(self):
				search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
				pages = search.pagination(0, 20, 10)
				urls = []
				for page in pages:
					urls.append(page['serpapi_pagination']['next'])
				self.assertEqual(len(urls), 2)
				self.assertTrue("start=10" in urls[0])
				print(urls[1])
				self.assertTrue("start=21" in urls[1])

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
				data = search.get_json()
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNone(data.get("error"))
				self.assertIsNotNone(data["search_metadata"]["google_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])
				self.assertIsNotNone(data['local_results']['places'][0])

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = GoogleSearch({"q": "Coffee", "engine": "google_scholar"})
				data = search.get_json()
				self.assertIsNotNone(data["organic_results"][0]["title"])

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_dict(self):
				search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
				data = search.get_dict()
				self.assertIsNotNone(data.get('local_results'))

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_dictionary(self):
				search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
				data = search.get_dictionary()
				self.assertIsNotNone(data.get('local_results'))

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_html(self):
				search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
				data = search.get_html()
				self.assertGreater(len(data), 10)

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_response(self):
				search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
				response = search.get_response()
				self.assertEqual(type(response), requests.Response)
				self.assertGreater(len(response.text), 10)

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_object(self):
				search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
				r = search.get_object()
				self.assertEqual(type(r.organic_results), list)
				self.assertIsNotNone(r.organic_results[0].title)
				self.assertIsNotNone(r.search_metadata.id)
				self.assertIsNotNone(r.search_metadata.google_url)
				self.assertEqual(r.search_parameters.q, "Coffee")
				self.assertEqual(r.search_parameters.engine, "google")
				self.assertGreater(r.search_information.total_results, 10)

if __name__ == '__main__':
		unittest.main()
