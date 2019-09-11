from lib.serp_api_client import *

class BaiduSearchResults(SerpApiClient):
    """GoogleSearchResults enables to search google and parse the result.
    ```python
    from lib.baidu_search_results import BaiduSearchResults
    query = BaiduSearchResults({"q": "coffee"})
    data = query.get_json()
    ```

    doc: https://serpapi.com/baidu-search-api
    """

    def __init__(self, params_dict):
        super().__init__(params_dict, BAIDU_ENGINE)

    def get_location(self, q, limit = 5):
        raise "location is not supported by Baidu search engine at this time"
