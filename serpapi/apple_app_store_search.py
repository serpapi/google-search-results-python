from .serp_api_client import SerpApiClient
from .serp_api_client_exception import SerpApiClientException
from .constant import APPLE_APP_STORE_ENGINE


class AppleAppStoreSearch(SerpApiClient):
    """AppleAppStoreSearch enables to search google scholar and parse the result.
    ```python
    from serpapi import AppleAppStoreSearch
    search = AppleAppStoreSearch({"term": "ipad"})
    data = search.get_dct()
    ```

    doc: https://serpapi.com/apple-app-store
    """

    def __init__(self, params_dict):
        super(AppleAppStoreSearch, self).__init__(params_dict, APPLE_APP_STORE_ENGINE)

    def get_location(self, q, limit=5):
        raise SerpApiClientException(
            "location is not supported by youtube search engine"
        )
