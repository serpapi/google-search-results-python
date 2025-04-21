import unittest
import os
from serpapi import YoutubeSearch


class TestYoutubeSearchApi(unittest.TestCase):
    def setUp(self):
        YoutubeSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_json(self):
        search = YoutubeSearch({"search_query": "chair"})
        data = search.get_dict()
        self.assertIsNone(data.get("error"))
        self.assertEqual(data["search_metadata"]["status"], "Success")
        self.assertIsNotNone(data["search_metadata"]["youtube_url"])
        self.assertIsNotNone(data["search_metadata"]["id"])

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_get_object(self):
        search = YoutubeSearch({"search_query": "chair"})
        data = search.get_object()
        self.assertEqual(data.search_metadata.status, "Success")
        self.assertIsNotNone(data.search_metadata.id)
        self.assertIsNotNone(data.search_metadata.youtube_url)
        self.assertEqual(data.search_parameters.search_query, "chair")
        self.assertEqual(data.search_parameters.engine, "youtube")
        self.assertGreater(data.search_information.total_results, 10)

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    def test_paginate(self):
        search = YoutubeSearch({"search_query": "chair"})

        limit = 3
        pages = search.pagination(limit=limit)

        titles = []

        page_count = 0
        count = 0

        for page in pages:
            page_count += 1

            for video_result in page.get("video_results", []):
                count += 1
                title_index = 0

                for title in titles:
                    title_index += 1

                    if title == video_result.get("title"):
                        print(
                            "%d duplicated title: %s at index: %d"
                            % (count, title, title_index)
                        )

                titles.append(video_result.get("title"))

        self.assertEqual(page_count, limit, "Number of pages doesn't match.")


if __name__ == "__main__":
    unittest.main()
