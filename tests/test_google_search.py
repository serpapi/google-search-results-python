import unittest
import os
import niquests as requests
from serpapi import GoogleSearch


class TestSearchApi(unittest.TestCase):

    def setUp(self):
        GoogleSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_paginate(self):
        page_size = 20
        search = GoogleSearch(
            {"q": "Coffee", "location": "Austin,Texas", "start": 10, "num": page_size}
        )

        limit = 2
        pages = search.pagination(limit=limit)

        page_count = 0

        for page in pages:
            page_count += 1

        self.assertEqual(page_count, limit)

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_json(self):
        search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
        data = search.get_json()
        self.assertEqual(data["search_metadata"]["status"], "Success")
        self.assertIsNone(data.get("error"))
        self.assertIsNotNone(data["search_metadata"]["google_url"])
        self.assertIsNotNone(data["search_metadata"]["id"])
        self.assertIsNotNone(data["local_results"]["places"][0])

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_json_2(self):
        search = GoogleSearch({"q": "Coffee", "engine": "google_scholar"})
        data = search.get_json()

        for organic_result in data["organic_results"]:
            self.assertIsNotNone(organic_result["title"])

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_dict(self):
        search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
        data = search.get_dict()
        self.assertIsNotNone(data.get("local_results"))

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_dictionary(self):
        search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
        data = search.get_dictionary()
        self.assertIsNotNone(data.get("local_results"))

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_html(self):
        search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
        data = search.get_html()
        self.assertGreater(len(data), 10)
        self.assertIn("<html", data)

        data = search.get_dict()
        self.assertEqual(data["search_metadata"]["status"], "Success")
        self.assertIsNone(data.get("error"))

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_response(self):
        search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
        response = search.get_response()
        self.assertEqual(type(response), requests.Response)
        self.assertGreater(len(response.text), 10)

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_object(self):
        search = GoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
        r = search.get_object()
        self.assertEqual(type(r.organic_results), list)
        self.assertIsNotNone(r.organic_results[0].title)
        self.assertIsNotNone(r.search_metadata.id)
        self.assertIsNotNone(r.search_metadata.google_url)
        self.assertEqual(r.search_parameters.q, "Coffee")
        self.assertEqual(r.search_parameters.engine, "google")
        self.assertGreater(r.search_information.total_results, 10)


if __name__ == "__main__":
    unittest.main()
