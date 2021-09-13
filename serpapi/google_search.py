from serpapi.serp_api_client import *
from serpapi.constant import *

class GoogleSearch(SerpApiClient):
    """GoogleSearch enables to search google and parse the result.
    ```python
    from serpapi import GoogleSearch
    search = GoogleSearch({"q": "coffee", "location": "Austin,Texas"})
    data = search.get_json()
    ```

    https://github.com/serpapi/google-search-results-python
    """

    def __init__(self, params_dict):
        super(GoogleSearch, self).__init__(params_dict, GOOGLE_ENGINE)
