import unittest
import os
from serpapi import AsyncBingSearch


class TestAsyncBingSearchApi(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        AsyncBingSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    async def test_get_json(self):
        search = AsyncBingSearch({"q": "Coffee", "location": "Austin,Texas"})
        data = await search.get_json()
        self.assertIsNone(data.get("error"))
        self.assertEqual(data["search_metadata"]["status"], "Success")
        self.assertIsNotNone(data["search_metadata"]["bing_url"])
        self.assertIsNotNone(data["search_metadata"]["id"])
        self.assertIsNotNone(data["organic_results"][0]["title"])
        # pp = pprint.PrettyPrinter(indent=2)
        # pp.pprint(data)

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    async def test_paginate(self):
        page_size = 20
        search = AsyncBingSearch(
            {"q": "Coffee", "location": "Austin,Texas", "first": 10, "count": page_size}
        )

        limit = 4
        pages = search.pagination(limit=limit)

        page_count = 0
        result_count = 0

        async for page in pages:
            page_count += 1
            result_count += len(page["organic_results"])

        self.assertEqual(page_count, limit)


if __name__ == "__main__":
    unittest.main()
