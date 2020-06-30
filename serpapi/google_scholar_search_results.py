from serpapi.serp_api_client import *

class GoogleScholarSearchResults(SerpApiClient):
    """GoogleScholarSearchResults enables to search google scholar and parse the result.
    ```python
    from serpapi.google_scholar_search_results import GoogleScholarSearchResults
    query = GoogleScholarSearchResults({"q": "coffee"})
    data = query.get_json()
    ```

    doc: https://serpapi.com/google-scholar-api
    """

    def __init__(self, params_dict):
        super(GoogleScholarSearchResults, self).__init__(params_dict, GOOGLE_SCHOLAR_ENGINE)

    def get_location(self, q, limit = 5):
        raise "location is not supported by Google scholar search engine"
