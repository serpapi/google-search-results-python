import random
import unittest
import os
from lib.google_search_results import GoogleSearchResults

class TestLocationApi(unittest.TestCase):

    def setUp(self):
        GoogleSearchResults.SERP_API_KEY = os.getenv("API_KEY","demo")

    def test_get_location(self):
        gsr = GoogleSearchResults({})
        location_list = gsr.get_location("Austin", 3)
        print(type(location_list))
        self.assertIsNotNone(location_list[0].get("id"))

if __name__ == '__main__':
    unittest.main()
