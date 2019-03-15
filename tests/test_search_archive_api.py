import random
import unittest
import os
from lib.google_search_results import GoogleSearchResults

class TestSearchArchiveApi(unittest.TestCase):

    def setUp(self):
        GoogleSearchResults.SERP_API_KEY = os.getenv("API_KEY","demo")

    def test_get_search_archive(self):
        gsr = GoogleSearchResults({"q": "Coffee", "location": "Austin,Texas"})
        search_result = gsr.get_dictionary()
        search_id = search_result.get("search_metadata").get("id")
        archived_search_result = GoogleSearchResults({}).get_search_archive(search_id, 'json')
        self.assertEqual(archived_search_result.get("search_metadata").get("id"), search_id)

if __name__ == '__main__':
    unittest.main()
