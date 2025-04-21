import unittest
import pprint
import os
from serpapi import AsyncGoogleSearch


class TestAsyncLocationApi(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        AsyncGoogleSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

    async def test_get_location(self):
        search = AsyncGoogleSearch({"q": None, "async": True})
        location_list = await search.get_location("Austin", 3)
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(location_list)
        self.assertIsNotNone(location_list[0].get("id"))


if __name__ == "__main__":
    unittest.main()
