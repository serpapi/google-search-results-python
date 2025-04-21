import unittest
import os
from serpapi import EbaySearch


class TestEbaySearchApi(unittest.TestCase):

    def setUp(self):
        EbaySearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_json(self):
        search = EbaySearch({"_nkw": "Coffee"})
        data = search.get_json()
        self.assertIsNone(data.get("error"))
        self.assertEqual(data["search_metadata"]["status"], "Success")
        self.assertIsNotNone(data["search_metadata"]["ebay_url"])
        self.assertIsNotNone(data["search_metadata"]["id"])
        self.assertIsNotNone(data["organic_results"][0]["title"])

        for organic_result in data.get("organic_results", []):
            self.assertIsNotNone(organic_result.get("title"))

        # pp = pprint.PrettyPrinter(indent=2)
        # pp.pprint(data)

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_paginate(self):
        page_size = 60

        params = {
            "_nkw": "coffee",
            "_ipg": page_size,
        }

        search = EbaySearch(params)

        limit = 3
        pages = search.pagination(limit=limit)

        page_count = 0
        result_count = 0

        for page in pages:
            page_count += 1
            result_count += len(page["organic_results"])

        self.assertEqual(page_count, limit)
        self.assertEqual(result_count, page_size * limit)


if __name__ == "__main__":
    unittest.main()
