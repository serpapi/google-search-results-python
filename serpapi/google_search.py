from serpapi.serp_api_client import *

class GoogleSearch(SerpApiClient):
    """GoogleSearch enables to search google and parse the result.
    ```python
    from serpapi import GoogleSearch
    query = GoogleSearch(
        {
            "q": "coffee",
            "location": "Austin,Texas",
        },
        timeout = 60,
        ssl_verify = True,
    )
    data = query.get_json()
    ```

    https://github.com/serpapi/google-search-results-python
    """

    def __init__(self, params_dict, timeout = 60, ssl_verify = True):
        super(GoogleSearch, self).__init__(params_dict, GOOGLE_ENGINE, timeout, ssl_verify)
