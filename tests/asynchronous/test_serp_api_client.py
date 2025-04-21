import unittest
import os
import pprint
from serpapi import AsyncSerpApiClient
from serpapi.serp_api_client_exception import SerpApiClientException
import pytest


# This test shows how to extends SerpApiClient
#  without using search engine wrapper.
#
class TestAsyncSerpSearchApi(unittest.IsolatedAsyncioTestCase):

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    async def test_get_json(self):
        search = AsyncSerpApiClient(
            {
                "q": "Coffee",
                "location": "Austin,Texas",
                "engine": "google_scholar",
                "api_key": os.getenv("API_KEY"),
            }
        )
        data = await search.get_json()
        assert data.get("error") is None
        self.assertIsNotNone(data["organic_results"][0]["title"])

    async def test_invalid_api_key(self):
        search = AsyncSerpApiClient(
            {
                "q": "Coffee",
                "location": "USA",
                "engine": "google",
                "api_key": "invalid_api_key",
            }
        )
        data = await search.get_json()
        self.assertIsNotNone(data["error"])

    async def test_error_missing_engine(self):
        search = AsyncSerpApiClient({"q": "Coffee", "api_key": os.getenv("API_KEY")})
        with pytest.raises(SerpApiClientException):
            await search.get_json()

    async def test_missing_(self):
        search = AsyncSerpApiClient(
            {"location": "USA", "engine": "google", "api_key": os.getenv("API_KEY")}
        )
        data = await search.get_json()
        self.assertIsNotNone(data["error"])
        self.assertRegex(data["error"], "Missing query `q`")

    def debug(self, payload):
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(payload)


if __name__ == "__main__":
    unittest.main()
