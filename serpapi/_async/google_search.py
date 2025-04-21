from .serp_api_client import *

class AsyncGoogleSearch(AsyncSerpApiClient):
    """AsyncGoogleSearch enables to search google and parse the result.
    ```python
    from serpapi import AsyncGoogleSearch
    query = AsyncGoogleSearch({"q": "coffee", "location": "Austin,Texas"})
    data = await query.get_json()
    ```

    https://github.com/serpapi/google-search-results-python
    """

    def __init__(self, params_dict):
        super(AsyncGoogleSearch, self).__init__(params_dict, GOOGLE_ENGINE)
