from .serp_api_client import AsyncSerpApiClient
from ..serp_api_client_exception import SerpApiClientException
from ..constant import WALMART_ENGINE


class AsyncWalmartSearch(AsyncSerpApiClient):
    """AsyncWalmartSearch enables to search google scholar and parse the result.
    ```python
    from serpapi import AsyncWalmartSearch
    search = AsyncWalmartSearch({"query": "chair"})
    data = await search.get_dict()
    ```

    doc: https://serpapi.com/walmart-search-api
    """

    def __init__(self, params_dict):
        super(AsyncWalmartSearch, self).__init__(params_dict, WALMART_ENGINE)

    async def get_location(self, q, limit=5):
        raise SerpApiClientException(
            "location is not supported by walmart search engine"
        )
