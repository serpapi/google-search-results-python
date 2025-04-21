from .serp_api_client import SerpApiClient
from .serp_api_client_exception import SerpApiClientException
from .constant import YANDEX_ENGINE


class YandexSearch(SerpApiClient):
    """YandexSearch enables to search yandex and parse the result.
    ```python
    from serpapi import YandexSearch
    query = YandexSearch({"text": "coffee"})
    data = query.get_json()
    ```

    doc: https://serpapi.com/yandex-search-api
    """

    def __init__(self, params_dict):
        super(YandexSearch, self).__init__(params_dict, YANDEX_ENGINE)

    def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by Yandex search engine at this time")
