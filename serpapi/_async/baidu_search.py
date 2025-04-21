from .serp_api_client import AsyncSerpApiClient
from serpapi.serp_api_client_exception import SerpApiClientException
from ..constant import BAIDU_ENGINE


class AsyncBaiduSearch(AsyncSerpApiClient):
    """BaiduSearch enables to search baidu and parse the result.
    ```python
    from serpapi import BaiduSearch
    query = AsyncBaiduSearch({"q": "coffee"})
    data = await query.get_json()
    ```

    doc: https://serpapi.com/baidu-search-api
    """

    def __init__(self, params_dict):
        super(AsyncBaiduSearch, self).__init__(params_dict, BAIDU_ENGINE)

    async def get_location(self, q, limit = 5):
        raise SerpApiClientException("location is not supported by Baidu search engine at this time")
