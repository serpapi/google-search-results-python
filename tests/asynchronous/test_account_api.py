import unittest
import os
from serpapi import AsyncGoogleSearch


class TestAsyncAccountApi(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        AsyncGoogleSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    async def test_get_account(self):
        search = AsyncGoogleSearch({})
        account = await search.get_account()
        self.assertIsNotNone(account.get("account_id"))
        self.assertEqual(account.get("api_key"), AsyncGoogleSearch.SERP_API_KEY)


if __name__ == "__main__":
    unittest.main()
