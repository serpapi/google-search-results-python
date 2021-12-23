from serpapi.serp_api_client import *
from serpapi.serp_api_client_exception import SerpApiClientException
from serpapi.constant import *

class DuckDuckGoSearch(SerpApiClient):
    """DuckDuckGoSearch enables to search google scholar and parse the result.
    ```python
    from serpapi import DuckDuckGoSearch
    search = DuckDuckGoSearch({"query": "chair"})
    data = search.get_json()
    ```

    doc: https://serpapi.com/duckduckgo-search-api
    """

    def __init__(self, params_dict):
        super(DuckDuckGoSearch, self).__init__(params_dict, DUCKDUCKGO_ENGINE)

    def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by walmart search engine")
