from .serp_api_client import *
from ..serp_api_client_exception import SerpApiClientException

class AsyncGoogleScholarSearch(AsyncSerpApiClient):
    """AsyncGoogleScholarSearch enables to search google scholar and parse the result.
    ```python
    from serpapi import AsyncGoogleScholarSearch
    query = AsyncGoogleScholarSearch({"q": "coffee"})
    data = await query.get_json()
    ```

    doc: https://serpapi.com/google-scholar-api
    """

    def __init__(self, params_dict):
        super(AsyncGoogleScholarSearch, self).__init__(params_dict, GOOGLE_SCHOLAR_ENGINE)

    async def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by Google scholar search engine")
