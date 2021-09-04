from serpapi.serp_api_client import *
from serpapi.serp_api_client_exception import SerpApiClientException

class YoutubeSearch(SerpApiClient):
    """YoutubeSearch enables to search google scholar and parse the result.
    ```python
    from serpapi import YoutubeSearch
    query = YoutubeSearch({"q": "chair"})
    data = query.get_json()
    ```

    doc: https://serpapi.com/youtube-search-api
    """

    def __init__(self, params_dict):
        super(YoutubeSearch, self).__init__(params_dict, YOUTUBE_ENGINE)

    def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by youtube search engine")
