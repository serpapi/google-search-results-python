from serpapi.serp_api_client import *
from serpapi.serp_api_client_exception import SerpApiClientException

class YahooSearch(SerpApiClient):
    """YahooSearch enables to search yahoo and parse the result.
    ```python
    from serpapi import YahooSearch
    query = YahooSearch({"p": "coffee"})
    data = query.get_json()
    ```

    doc: https://serpapi.com/yahoo-search-api
    """

    def __init__(self, params_dict):
        super(YahooSearch, self).__init__(params_dict, YAHOO_ENGINE)

    def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by Yahoo search engine at this time")
