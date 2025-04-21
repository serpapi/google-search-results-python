from .serp_api_client import AsyncSerpApiClient
from ..serp_api_client_exception import SerpApiClientException
from ..constant import NAVER_ENGINE


class AsyncNaverSearch(AsyncSerpApiClient):
    """NaverSearch enables to search on naver and parse the result.
    ```python
    from serpapi import AsyncNaverSearch
    search = AsyncNaverSearch({"query": "chair"})
    data = await search.get_dict()
    ```

    doc: https://serpapi.com/naver-search-api
    """

    def __init__(self, params_dict):
        super(AsyncNaverSearch, self).__init__(params_dict, NAVER_ENGINE)

    async def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by naver search engine")
