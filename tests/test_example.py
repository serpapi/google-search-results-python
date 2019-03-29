import random
import unittest
import os
from lib.google_search_results import GoogleSearchResults

class TestExample(unittest.TestCase):

    def setUp(self):
        GoogleSearchResults.SERP_API_KEY = os.getenv("API_KEY","demo")

    def test_async(self):
        gsr = GoogleSearchResults({"q": "Coffee", "location": "Austin,Texas"})
        results = gsr.get_json()
        self.assertIsNotNone(results["local_results"][0]["title"])

if __name__ == '__main__':
    unittest.main()
