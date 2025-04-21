from .serp_api_client import AsyncSerpApiClient
from ..serp_api_client_exception import SerpApiClientException
from ..constant import YANDEX_ENGINE


class AsyncYandexSearch(AsyncSerpApiClient):
    """AsyncYandexSearch enables to search yandex and parse the result.
    ```python
    from serpapi import AsyncYandexSearch
    query = AsyncYandexSearch({"text": "coffee"})
    data = await query.get_json()
    ```

    doc: https://serpapi.com/yandex-search-api
    """

    def __init__(self, params_dict):
        super(AsyncYandexSearch, self).__init__(params_dict, YANDEX_ENGINE)

    async def get_location(self, q, limit=5):
        raise SerpApiClientException(
            "location is not supported by Yandex search engine at this time"
        )
