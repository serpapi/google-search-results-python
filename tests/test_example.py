import random
import unittest
import os
import wget
from lib.google_search_results import GoogleSearchResults

class TestExample(unittest.TestCase):

    def setUp(self):
        GoogleSearchResults.SERP_API_KEY = os.getenv("API_KEY","demo")

    @unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
    def test_search_google_images(self):
        client = GoogleSearchResults({"q": "coffe", "tbm": "isch"})
        for image_result in client.get_json()['images_results']:
            link = image_result["original"]
            try:
                print("link: " + link)
                # wget.download(link, '.')
            except:
                pass
            # https://github.com/serpapi/showcase-serpapi-tensorflow-keras-image-training/blob/master/fetch.py

    # @unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
    # def test_async(self):
    #     client = GoogleSearchResults({
    #         "q": "Coffee", 
    #         "location": "Austin,Texas", 
    #         "async": True
    #     })
    #     results = client.get_json()
    #     self.assertIsNotNone(results["local_results"][0]["title"])

    @unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
    def test_search_google_news(self):
        client = GoogleSearchResults({
            "q": "coffe",   # search client
            "tbm": "nws",  # news
            "tbs": "qdr:d", # last 24h
            "num": 10
        })
        for offset in [0,1,2]:
            client.params_dict["start"] = offset * 10
            data = client.get_json()
            for news_result in data['news_results']:
                print(str(news_result['position'] + offset * 10) + " - " + news_result['title'])

    @unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
    def test_search_google_shopping(self):
        client = GoogleSearchResults({
            "q": "coffe",   # search client
            "tbm": "shop",  # news
            "tbs": "p_ord:rv", # last 24h
            "num": 100
        })
        data = client.get_json()
        for shopping_result in data['shopping_results']:
            print(str(shopping_result['position']) + " - " + shopping_result['title'])

    @unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
    def test_search_by_location(self):
        for city in ["new york", "paris", "berlin"]:
            location = GoogleSearchResults({}).get_location(city, 1)[0]["canonical_name"]
            client = GoogleSearchResults({
                "q": "best coffee shop",   # search client
                "location": location,
                "num": 1,
                "start": 0
            })
            data = client.get_json()
            top_result = data["organic_results"][0]["title"]
            print("top coffee result for " + location + " is: " + top_result)


if __name__ == '__main__':
    unittest.main()
