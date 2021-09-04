import random
import unittest
import os
import pprint
from serpapi import SerpApiClient
from serpapi.serp_api_client_exception import SerpApiClientException
import pytest

# This test shows how to extends SerpApiClient
#  without using search engine wrapper.
# 
class TestSerpSearchApi(unittest.TestCase):

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
			search = SerpApiClient({
				"q": "Coffee", 
				"location": "Austin,Texas", 
				"engine": "google_scholar",
				"api_key": os.getenv("API_KEY")
				})
			data = search.get_json()
			assert data.get("error") == None
			self.assertIsNotNone(data["organic_results"][0]["title"])

		def test_invalid_api_key(self):
			search = SerpApiClient({
				"q": "Coffee", 
				"location": "USA", 
				"engine": "google",
				"api_key": "invalid_api_key"
			})
			data = search.get_json()
			self.assertIsNotNone(data["error"])

		def test_error_missing_engine(self):
			search = SerpApiClient({
				"q": "Coffee", 
				"api_key": os.getenv("API_KEY")
			})
			with pytest.raises(SerpApiClientException):
				search.get_json()

		def test_missing_(self):
			search = SerpApiClient({
				"location": "USA", 
				"engine": "google",
				"api_key": os.getenv("API_KEY")
			})
			data = search.get_json()
			self.assertIsNotNone(data["error"])
			self.assertRegex(data["error"], "Missing query `q`")

		def debug(self, payload):
			pp = pprint.PrettyPrinter(indent=2)
			pp.pprint(payload)

if __name__ == '__main__':
		unittest.main()
