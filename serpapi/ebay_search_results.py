from serpapi.serp_api_client import *

class EbaySearchResults(SerpApiClient):
    """EbaySearchResults enables to search ebay and parse the result.
    ```python
    from serpapi.ebay_search_results import EbaySearchResults
    query = EbaySearchResults({"_nkw": "coffee"})
    data = query.get_json()
    ```

    doc: https://serpapi.com/ebay-search-api
    """

    def __init__(self, params_dict):
        super(EbaySearchResults, self).__init__(params_dict, EBAY_ENGINE)

    def get_location(self, q, limit = 5):
        raise "location is not supported by Ebay search engine at this time"
