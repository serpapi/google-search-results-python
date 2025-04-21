from .serp_api_client import *
from ..serp_api_client_exception import SerpApiClientException

class AsyncEbaySearch(AsyncSerpApiClient):
    """EbaySearch enables to search ebay and parse the result.
    ```python
    from serpapi import AsyncEbaySearch
    query = AsyncEbaySearch({"_nkw": "coffee"})
    data = await query.get_json()
    ```

    doc: https://serpapi.com/ebay-search-api
    """

    def __init__(self, params_dict):
        super(AsyncEbaySearch, self).__init__(params_dict, EBAY_ENGINE)

    async def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by Ebay search engine at this time")
