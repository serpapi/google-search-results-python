from serpapi.serp_api_client import *
from serpapi.constant import *

class BingSearch(SerpApiClient):
    """BingSearch enables to search bing and parse the result.
    ```python
    from serpapi import BingSearch
    search = BingSearch({"q": "coffee", "location": "Austin,Texas"})
    data = search.get_json()
    ```

    doc: https://serpapi.com/bing-search-api
    """

    def __init__(self, params_dict):
        super(BingSearch, self).__init__(params_dict, BING_ENGINE)
