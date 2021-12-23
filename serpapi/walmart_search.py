from serpapi.serp_api_client import *
from serpapi.serp_api_client_exception import SerpApiClientException
from serpapi.constant import *

class WalmartSearch(SerpApiClient):
    """WalmartSearch enables to search google scholar and parse the result.
    ```python
    from serpapi import WalmartSearch
    search = WalmartSearch({"query": "chair"})
    data = search.get_dict()
    ```

    doc: https://serpapi.com/walmart-search-api
    """

    def __init__(self, params_dict):
        super(WalmartSearch, self).__init__(params_dict, WALMART_ENGINE)

    def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by walmart search engine")
