import unittest
import os
import pprint
from serpapi import YandexSearch


class TestYandexSearchApi(unittest.TestCase):

    def setUp(self):
        YandexSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_json(self):
        search = YandexSearch({"text": "Coffee"})
        data = search.get_json()
        self.assertIsNone(data.get("error"))
        self.assertEqual(data["search_metadata"]["status"], "Success")
        self.assertIsNotNone(data["search_metadata"]["yandex_url"])
        self.assertIsNotNone(data["search_metadata"]["id"])
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(data["organic_results"])

        for organic_result in data.get("organic_results", []):
            self.assertIsNotNone(organic_result.get("title"))

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_paginate(self):
        search = YandexSearch({"text": "Coffee"})

        limit = 3
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
                            "%d duplicated title: %s at index: %d"
                            % (organic_results_count, title, title_index)
                        )

                titles.append(organic_result.get("title"))

        self.assertEqual(page_number, limit, "Number of pages doesn't match.")


if __name__ == "__main__":
    unittest.main()
