from serpapi.serp_api_client import *

class YandexSearchResults(SerpApiClient):
    """YandexSearchResults enables to search yandex and parse the result.
    ```python
    from serpapi.yandex_search_results import YandexSearchResults
    query = YandexSearchResults({"text": "coffee"})
    data = query.get_json()
    ```

    doc: https://serpapi.com/yandex-search-api
    """

    def __init__(self, params_dict):
        super(YandexSearchResults, self).__init__(params_dict, YANDEX_ENGINE)

    def get_location(self, q, limit = 5):
        raise "location is not supported by Yandex search engine at this time"
