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

    VERSION = "1.0.0"
    BACKEND = "https://serpapi.com/search"
    SERP_API_KEY = None

    def __init__(self, params_dict):
        self.params_dict = params_dict

    def construct_url(self):
        self.params_dict['source'] = 'python'
        if self.SERP_API_KEY:
            self.params_dict['serp_api_key'] = self.SERP_API_KEY
        response = requests.get(self.BACKEND, self.params_dict, timeout=600)
        return response.text

    def get_results(self):
        try:
            self.construct_url()
        except requests.HTTPError as e:
            print(e, e.response.status_code)
        return self.construct_url()

    def get_html(self):
        return self.get_results()

    def get_json(self):
        """Returns:
            JSON with the formatted response content
        """
        self.params_dict["output"] = "json"
        return json.loads(self.get_results())

    def get_dictionary(self):
        """Returns:
            Dict with the formatted response content
        """
        return dict(self.get_json())
