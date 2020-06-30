import random
import unittest
import os
import pprint
from serpapi import GoogleScholarSearchResults
   
class TestGoogleScholarSearchResults(unittest.TestCase):

		def setUp(self):
				GoogleScholarSearchResults.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				client = GoogleScholarSearchResults({"q": "Coffee"})
				data = client.get_json()
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["id"])
				self.assertIsNotNone(data["organic_results"][0]["title"])

if __name__ == '__main__':
		unittest.main()
