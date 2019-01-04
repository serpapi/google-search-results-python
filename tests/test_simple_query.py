import random
import unittest
from lib.google_search_results import GoogleSearchResults

class TestSimpleQuery(unittest.TestCase):

    def setUp(self):
        GoogleSearchResults.SERP_API_KEY = "demo"

    def test_get_json(self):
        query = GoogleSearchResults({"q": "Coffee", "location": "Austin,Texas"})
        results = query.get_json()
        self.assertIsNotNone(results["local_results"][0]["title"])

if __name__ == '__main__':
    unittest.main()
