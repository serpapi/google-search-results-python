from serpapi.serp_api_client import *
from serpapi.serp_api_client_exception import SerpApiClientException
from serpapi.constant import *

class BaiduSearch(SerpApiClient):
    """BaiduSearch enables to search baidu and parse the result.
    ```python
    from serpapi import BaiduSearch
    search = BaiduSearch({"q": "coffee"})
    data = search.get_json()
    ```

    doc: https://serpapi.com/baidu-search-api
    """

    def __init__(self, params_dict):
        super(BaiduSearch, self).__init__(params_dict, BAIDU_ENGINE)

    def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by Baidu search engine at this time")
