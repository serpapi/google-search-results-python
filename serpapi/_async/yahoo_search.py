from .serp_api_client import AsyncSerpApiClient
from ..serp_api_client_exception import SerpApiClientException
from ..constant import YAHOO_ENGINE


class AsyncYahooSearch(AsyncSerpApiClient):
    """AsyncYahooSearch enables to search yahoo and parse the result.
    ```python
    from serpapi import AsyncYahooSearch
    query = AsyncYahooSearch({"p": "coffee"})
    data = await query.get_json()
    ```

    doc: https://serpapi.com/yahoo-search-api
    """

    def __init__(self, params_dict):
        super(AsyncYahooSearch, self).__init__(params_dict, YAHOO_ENGINE)

    async def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by Yahoo search engine at this time")
