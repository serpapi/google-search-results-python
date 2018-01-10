import os
import requests

class GoogleSearchResults(object):
    VERSION = "1.0.0"
    BACKEND = "http://serpapi.com/search"
    SERP_API_KEY = None

    def __init__(self, params_dict):
        self.params_dict = params_dict

    def construct_url(self):
        self.params_dict['source'] = 'python'
        if GoogleSearchResults.SERP_API_KEY:
            self.params_dict['serp_api_key'] = self.SERP_API_KEY
        response = requests.get(self.BACKEND, self.params_dict)
        return response.text

    def get_results(self):
        try:
            self.construct_url()
        except requests.HTTPError as e:
            print e, e.response.status_code
        return self.construct_url()

    def get_html(self):
        return self.get_results()

    def get_json(self):
        self.params_dict["output"] = "json"
        return self.get_results()

    def get_json_with_images(self):
        self.params_dict["output"] = "json_with_images"
        return self.get_results()

    def get_dictionary(self):
        return json.loads(dict(get_json))

    def get_dictionary_with_images(self):
        return json.loads(dict(get_json_with_images))
