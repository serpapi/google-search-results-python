from .serp_api_client import SerpApiClient
from .serp_api_client_exception import SerpApiClientException
from .constant import EBAY_ENGINE


class EbaySearch(SerpApiClient):
    """EbaySearch enables to search ebay and parse the result.
    ```python
    from serpapi import EbaySearch
    query = EbaySearch({"_nkw": "coffee"})
    data = query.get_json()
    ```

    doc: https://serpapi.com/ebay-search-api
    """

    def __init__(self, params_dict):
        super(EbaySearch, self).__init__(params_dict, EBAY_ENGINE)

    def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by Ebay search engine at this time")
