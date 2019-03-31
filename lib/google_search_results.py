import requests
import json

class GoogleSearchResults(object):
    """GoogleSearchResults enables to search google and parse the result.
    ```python
    from lib.google_search_results import GoogleSearchResults
    query = GoogleSearchResults({"q": "coffee", "location": "Austin,Texas"})
    data = query.get_json()
    ```

    https://github.com/serpapi/google-search-results-python
    """

    VERSION = "1.4.0"
    BACKEND = "https://serpapi.com"
    SERP_API_KEY = None

    def __init__(self, params_dict):
        self.params_dict = params_dict

    def construct_url(self, path = "/search"):
        self.params_dict['source'] = 'python'
        if self.SERP_API_KEY:
            self.params_dict['serp_api_key'] = self.SERP_API_KEY
        return self.BACKEND + path, self.params_dict

    def get_results(self, path = '/search'):
        url = None
        try:
            url, parameter = self.construct_url(path)
            response = requests.get(url, parameter, timeout=60000)
            return response.text
        except requests.HTTPError as e:
            print("fail: " + url)
            print(e, e.response.status_code)
            raise e

    def get_html(self):
        """Returns:
            Raw HTML search result from Gooogle
        """
        return self.get_results()

    def get_json(self):
        """Returns:
            Formatted JSON search result
        """
        self.params_dict["output"] = "json"
        return json.loads(self.get_results())

    def get_dictionary(self):
        """Returns:
            Dict with the formatted response content
        """
        return dict(self.get_json())

    def get_dict(self):
        """Returns:
            Dict with the formatted response content
        """
        return self.get_dictionary()

    def get_location(self, q, limit = 5):
        """Get location using Location API
        Parameters:
            q (string): location (like: city name..)
            limit (int): number of matches returned
        Returns:
            Dict: Location matching q
        """
        self.params_dict = {}
        self.params_dict["output"] = "json"
        self.params_dict["q"] = q
        self.params_dict["limit"] = limit
        return json.loads(self.get_results('/locations.json'))

    def get_search_archive(self, search_id, format = 'json'):
        """Retrieve search result from the Search Archive API
        Parameters:
            search_id (int): unique identifier for the search provided by metadata.id 
            format (string): search format: json or html [optional]
        Returns:
            dict|string: search result from the archive
        """
        return json.loads(self.get_results("/searches/{0}.{1}".format(search_id, format)))

    def get_account(self):
        """Get account information using Account API
        Returns:
            dict: account information
        """
        return json.loads(self.get_results("/account"))
