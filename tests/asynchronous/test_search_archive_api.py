import unittest
import os
from serpapi import AsyncGoogleSearch


class TestAsyncSearchArchiveApi(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        AsyncGoogleSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

    @unittest.skipIf((os.getenv("API_KEY") is None), "no api_key provided")
    async def test_get_search_archive(self):
        search = AsyncGoogleSearch({"q": "Coffee", "location": "Austin,Texas"})
        search_result = await search.get_dictionary()
        search_id = search_result.get("search_metadata").get("id")
        archived_search_result = await AsyncGoogleSearch({}).get_search_archive(
            search_id, "json"
        )
        self.assertEqual(
            archived_search_result.get("search_metadata").get("id"), search_id
        )
        html_buffer = await AsyncGoogleSearch({}).get_search_archive(search_id, "html")
        self.assertGreater(len(html_buffer), 10000)


if __name__ == "__main__":
    unittest.main()
