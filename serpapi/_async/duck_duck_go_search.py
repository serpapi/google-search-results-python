from .serp_api_client import AsyncSerpApiClient
from ..serp_api_client_exception import SerpApiClientException
from ..constant import DUCKDUCKGO_ENGINE


class AsyncDuckDuckGoSearch(AsyncSerpApiClient):
    """AsyncDuckDuckGoSearch enables to search duckduckgo and parse the result.
    ```python
    from serpapi import DuckDuckGoSearch
    search = AsyncDuckDuckGoSearch({"query": "chair"})
    data = await search.get_json()
    ```

    doc: https://serpapi.com/duckduckgo-search-api
    """

    def __init__(self, params_dict):
        super(AsyncDuckDuckGoSearch, self).__init__(params_dict, DUCKDUCKGO_ENGINE)

    async def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by duckduckgo engine")
