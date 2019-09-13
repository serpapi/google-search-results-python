from lib.serp_api_client import *

class GoogleSearchResults(SerpApiClient):
    """GoogleSearchResults enables to search google and parse the result.
    ```python
    from lib.google_search_results import GoogleSearchResults
    query = GoogleSearchResults({"q": "coffee", "location": "Austin,Texas"})
    data = query.get_json()
    ```

    https://github.com/serpapi/google-search-results-python
    """

    def __init__(self, params_dict):
        super(GoogleSearchResults, self).__init__(params_dict, GOOGLE_ENGINE)
