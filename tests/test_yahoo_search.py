import unittest
import os
from serpapi import YahooSearch


class TestYahooSearchApi(unittest.TestCase):

    def setUp(self):
        YahooSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_json(self):
        search = YahooSearch({"p": "Coffee"})
        data = search.get_json()
        self.assertIsNone(data.get("error"))
        self.assertEqual(data["search_metadata"]["status"], "Success")
        self.assertIsNotNone(data["search_metadata"]["yahoo_url"])
        self.assertIsNotNone(data["search_metadata"]["id"])

        for organic_result in data.get("organic_results", []):
            self.assertIsNotNone(organic_result.get("title"))

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_paginate(self):
        page_size = 7
        search = YahooSearch({"p": "Coffee", "b": page_size, "pz": page_size})

        limit = 4
        pages = search.pagination(limit=limit)

        titles = []
        page_number = 0

        for page in pages:
            organic_results_count = 0
            page_number += 1

            for organic_result in page.get("organic_results", []):
                organic_results_count += 1
                title_index = 0

                for title in titles:
                    title_index += 1

                    if title == organic_result.get("title"):
                        print(
                            "Organic result #%d on page #%d contains duplicated title: %s at index: %d"
                            % (organic_results_count, page_number, title, title_index)
                        )

                titles.append(organic_result.get("title"))

        self.assertEqual(page_number, limit, "Number of pages doesn't match.")


if __name__ == "__main__":
    unittest.main()
