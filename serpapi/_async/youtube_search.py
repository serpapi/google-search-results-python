from .serp_api_client import *
from ..serp_api_client_exception import SerpApiClientException

class AsyncYoutubeSearch(AsyncSerpApiClient):
    """YoutubeSearch enables to search google scholar and parse the result.
    ```python
    from serpapi import AsyncYoutubeSearch
    query = AsyncYoutubeSearch({"search_query": "chair"})
    data = await query.get_dict()
    ```

    doc: https://serpapi.com/youtube-search-api
    """

    def __init__(self, params_dict):
        super(AsyncYoutubeSearch, self).__init__(params_dict, YOUTUBE_ENGINE)

    def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by youtube search engine")
