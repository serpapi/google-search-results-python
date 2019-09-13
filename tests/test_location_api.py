import random
import unittest
import pprint
import os
from serpapi.google_search_results import GoogleSearchResults

class TestLocationApi(unittest.TestCase):

    def setUp(self):
        GoogleSearchResults.SERP_API_KEY = os.getenv("API_KEY","demo")

    def test_get_location(self):
        client = GoogleSearchResults({"q": None, "async": True})
        location_list = client.get_location("Austin", 3)
        self.assertIsNotNone(location_list[0].get("id"))
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(location_list)

if __name__ == '__main__':
    unittest.main()
