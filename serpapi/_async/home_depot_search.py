from .serp_api_client import AsyncSerpApiClient
from ..serp_api_client_exception import SerpApiClientException
from ..constant import HOME_DEPOT_ENGINE


class AsyncHomeDepotSearch(AsyncSerpApiClient):
    """AsyncHomeDepotSearch enables to search home depot and parse the result.
    ```python
    from serpapi import AsyncHomeDepotSearch
    query = AsyncHomeDepotSearch({"q": "chair"})
    data = await query.get_json()
    ```

    doc: https://serpapi.com/home-depot-search-api
    """

    def __init__(self, params_dict):
        super(AsyncHomeDepotSearch, self).__init__(params_dict, HOME_DEPOT_ENGINE)

    async def get_location(self, q, limit=5):
        raise SerpApiClientException(
            "location is not supported by Home Depot search engine"
        )
