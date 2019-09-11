import random
import unittest
import os
import pprint
from lib.baidu_search_results import BaiduSearchResults

class TestBaiduSearchApi(unittest.TestCase):

		def setUp(self):
				BaiduSearchResults.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				client = BaiduSearchResults({"q": "Coffee"})
				data = client.get_json()
				self.assertIsNotNone(data["organic_results"][0]["title"])
				pp = pprint.PrettyPrinter(indent=2)
				pp.pprint(data)

if __name__ == '__main__':
		unittest.main()
