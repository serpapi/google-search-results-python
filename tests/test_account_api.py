import random
import unittest
import os
from serpapi import GoogleSearchResults

class TestAccountApi(unittest.TestCase):

    def setUp(self):
        GoogleSearchResults.SERP_API_KEY = os.getenv("API_KEY","demo")

    @unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
    def test_get_account(self):
        client = GoogleSearchResults({})
        account = client.get_account()
        self.assertIsNotNone(account.get("account_id"))
        self.assertEqual(account.get("api_key"), GoogleSearchResults.SERP_API_KEY)

if __name__ == '__main__':
    unittest.main()
