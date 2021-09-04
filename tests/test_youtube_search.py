import random
import unittest
import os
import pprint
from serpapi import YoutubeSearch

class TestYoutubeSearchApi(unittest.TestCase):

		def setUp(self):
				YoutubeSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = YoutubeSearch({"search_query": "chair"})
				data = search.get_dict()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["youtube_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_object(self):
				search = YoutubeSearch({"search_query": "chair"})
				data = search.get_object()
				self.assertEqual(data.search_metadata.status, "Success")
				self.assertIsNotNone(data.search_metadata.id)
				self.assertIsNotNone(data.search_metadata.youtube_url)
				self.assertEqual(data.search_parameters.search_query, "chair")
				self.assertEqual(data.search_parameters.engine, "youtube")
				self.assertGreater(data.search_information.total_results, 10)

if __name__ == '__main__':
		unittest.main()
