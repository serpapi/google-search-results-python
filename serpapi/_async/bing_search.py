from .serp_api_client import *

class AsyncBingSearch(AsyncSerpApiClient):
    """BingSearch enables to search bing and parse the result.
    ```python
    from serpapi import AsyncBingSearch
    query = AsyncBingSearch({"q": "coffee", "location": "Austin,Texas"})
    data = await query.get_json()
    ```

    doc: https://serpapi.com/bing-search-api
    """

    def __init__(self, params_dict):
        super(AsyncBingSearch, self).__init__(params_dict, BING_ENGINE)
