from serpapi.serp_api_client import *

class BingSearchResults(SerpApiClient):
    """BingSearchResults enables to search bing and parse the result.
    ```python
    from serpapi import BingSearchResults
    query = BingSearchResults({"q": "coffee", "location": "Austin,Texas"})
    data = query.get_json()
    ```

    doc: https://serpapi.com/bing-search-api
    """

    def __init__(self, params_dict):
        super(BingSearchResults, self).__init__(params_dict, BING_ENGINE)
