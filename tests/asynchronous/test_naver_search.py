import random
import unittest
import os
import pprint
from serpapi import AsyncNaverSearch

class TestAsyncNaverSearchApi(unittest.IsolatedAsyncioTestCase):

		def setUp(self):
				AsyncNaverSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		async def test_get_json(self):
				search = AsyncNaverSearch({"query": "Coffee"})
				data = await search.get_json()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["naver_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])

				for ad in data.get("ads_results", []):
					self.assertIsNotNone(ad["title"])

				for organic_result in data.get("web_results", []):
					self.assertIsNotNone(organic_result["title"])

				pp = pprint.PrettyPrinter(indent=2)
				pp.pprint(data)
				print(data.keys())

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		async def test_paginate_page_size(self):
			start = 24
			limit = 3

			# use parameters in
			params = {
				"query": "coffee",
				"start": start,
			}

			titles = []

			search = AsyncNaverSearch(params)
			pages = search.pagination(limit=limit)

			page_number = 0
			count = 0

			async for page in pages:
				page_number += 1

				for result in page.get("web_results", []):
					count += 1
					i = 0

					for item in titles:
						i += 1

						if item == result.get('title'):
							print("%d duplicated title: %s at index: %d" % (count, item, i))

					titles.append(result['title'])

			self.assertEqual(page_number, limit, "Number of pages doesn't match.")

if __name__ == '__main__':
		unittest.main()
