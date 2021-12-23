from serpapi.serp_api_client import *
from serpapi.serp_api_client_exception import SerpApiClientException
from serpapi.constant import *

class NaverSearch(SerpApiClient):
    """NaverSearch enables to search google scholar and parse the result.
    ```python
    from serpapi import NaverSearch
    search = NaverSearch({"query": "chair"})
    data = search.get_dict()
    ```

    doc: https://serpapi.com/naver-search-api
    """

    def __init__(self, params_dict):
        super(NaverSearch, self).__init__(params_dict, NAVER_ENGINE)

    def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by youtube search engine")
