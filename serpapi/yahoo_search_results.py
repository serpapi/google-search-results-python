from serpapi.serp_api_client import *

class YahooSearchResults(SerpApiClient):
    """YahooSearchResults enables to search yahoo and parse the result.
    ```python
    from serpapi import YahooSearchResults
    query = YahooSearchResults({"p": "coffee"})
    data = query.get_json()
    ```

    doc: https://serpapi.com/yahoo-search-api
    """

    def __init__(self, params_dict):
        super(YahooSearchResults, self).__init__(params_dict, YAHOO_ENGINE)

    def get_location(self, q, limit = 5):
        raise "location is not supported by Yahoo search engine at this time"
