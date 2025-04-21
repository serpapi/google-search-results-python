import niquests as requests
import json
from ..constant import DEFAULT_START, DEFAULT_END, DEFAULT_LIMIT, DEFAULT_PAGE_SIZE
from ._shared import DEFAULT_HTTP_CLIENT
from .pagination import AsyncPagination
from ..serp_api_client import SerpApiClient


class AsyncSerpApiClient(SerpApiClient):
    """SerpApiClient enables to query any search engines supported by SerpApi and parse the results.
    ```python
    from serpapi import AsyncSerpApiClient
    search = AsyncSerpApiClient({
        "q": "Coffee",
        "location": "Austin,Texas",
        "engine": "google",
        "api_key": "<your private key>"
        })
        data = await search.get_json()
    ```

    https://serpapi.com/search-api
    """

    def __init__(self, params_dict, engine=None, timeout=60000):
        super().__init__(params_dict, engine, timeout)

    async def get_response(self, path="/search"):
        """Returns:
        Response object provided by requests.get
        """
        url = None
        try:
            url, parameter = self.construct_url(path)
            return await DEFAULT_HTTP_CLIENT.get(
                url, params=parameter, timeout=self.timeout
            )
        except requests.HTTPError as e:
            print("fail: " + url)
            print(e, e.response.status_code)
            raise e

    async def get_results(self, path="/search"):
        """Returns:
        Response text field
        """
        return (await self.get_response(path)).text

    async def get_html(self):
        """Returns:
        Raw HTML search result from Google
        """
        self.params_dict["output"] = "html"
        return await self.get_results()

    async def get_json(self):
        """Returns:
        Formatted JSON search results using json package
        """
        self.params_dict["output"] = "json"
        return json.loads(await self.get_results())

    async def get_raw_json(self):
        """Returns:
        Formatted JSON search result as string
        """
        self.params_dict["output"] = "json"
        return await self.get_results()

    async def get_dictionary(self):
        """Returns:
        Dict with the formatted response content
        """
        return dict(await self.get_json())

    async def get_dict(self):
        """Returns:
        Dict with the formatted response content
        (alias for get_dictionary)
        """
        return await self.get_dictionary()

    async def get_object(self):
        """Returns:
        Dynamically created python object wrapping the result data structure
        """
        # iterative over response hash
        node = await self.get_dictionary()
        # create dynamic python object
        return self.make_pyobj("response", node)

    async def get_search_archive(self, search_id, format="json"):
        """Retrieve search result from the Search Archive API
        Parameters:
            search_id (int): unique identifier for the search provided by metadata.id
            format (string): search format: json or html [optional]
        Returns:
            dict|string: search result from the archive
        """
        result = await self.get_results("/searches/{0}.{1}".format(search_id, format))
        if format == "json":
            result = json.loads(result)
        return result

    async def get_account(self):
        """Get account information using Account API
        Returns:
            dict: account information
        """
        return json.loads(await self.get_results("/account"))

    async def get_location(self, q, limit=5):
        """Get location using Location API
        Parameters:
            q (string): location (like: city name..)
            limit (int): number of matches returned
        Returns:
            dict: Location matching q
        """
        self.params_dict = {}
        self.params_dict["output"] = "json"
        self.params_dict["q"] = q
        self.params_dict["limit"] = limit
        buffer = await self.get_results("/locations.json")
        return json.loads(buffer)

    def pagination(
        self,
        start=DEFAULT_START,
        end=DEFAULT_END,
        page_size=DEFAULT_PAGE_SIZE,
        limit=DEFAULT_LIMIT,
    ):
        """Return:
        Generator to iterate the search results pagination
        """
        return AsyncPagination(self, start, end, page_size, limit)
