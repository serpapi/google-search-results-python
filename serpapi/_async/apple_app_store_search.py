from .serp_api_client import AsyncSerpApiClient
from ..serp_api_client_exception import SerpApiClientException
from ..constant import APPLE_APP_STORE_ENGINE

class AsyncAppleAppStoreSearch(AsyncSerpApiClient):
    """AppleAppStoreSearch enables to search app store and parse the result.
    ```python
    from serpapi import AsyncAppleAppStoreSearch
    search = AsyncAppleAppStoreSearch({"term": "ipad"})
    data = await search.get_dct()
    ```
    
    doc: https://serpapi.com/apple-app-store
    """

    def __init__(self, params_dict):
        super(AsyncAppleAppStoreSearch, self).__init__(params_dict, APPLE_APP_STORE_ENGINE)

    async def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by apple appstore engine")
