import random
import unittest
import os
import pprint
from serpapi.google_search_results import GoogleSearchResults

class TestSearchApi(unittest.TestCase):

		def setUp(self):
				GoogleSearchResults.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				client = GoogleSearchResults({"q": "Coffee", "location": "Austin,Texas"})
				data = client.get_json()
				# pp = pprint.PrettyPrinter(indent=2)
				# pp.pprint(data['local_results'])
				self.assertIsNotNone(data['local_results']['places'][0])

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				client = GoogleSearchResults({"q": "Coffee", "engine": "google_scholar"})
				data = client.get_json()
				self.assertIsNotNone(data["organic_results"][0]["title"])

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_dict(self):
				client = GoogleSearchResults({"q": "Coffee", "location": "Austin,Texas"})
				data = client.get_dict()
				self.assertIsNotNone(data.get('local_results'))

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_dictionary(self):
				client = GoogleSearchResults({"q": "Coffee", "location": "Austin,Texas"})
				data = client.get_dictionary()
				self.assertIsNotNone(data.get('local_results'))

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_html(self):
				client = GoogleSearchResults({"q": "Coffee", "location": "Austin,Texas"})
				data = client.get_html()
				self.assertGreater(len(data), 10)

if __name__ == '__main__':
		unittest.main()
