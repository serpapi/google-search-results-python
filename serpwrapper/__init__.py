import os
import requests

TMDB_API_KEY = os.environ.get('SERP_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

# if TMDB_API_KEY is None:
#     raise APIKeyMissingError(
#         "All methods require an API key. Send an email "
#         "for how to retrieve an authentication token from "
#         "SERP API"
#     )
session = requests.Session()
session.params = {}
session.params['api_key'] = None #SERP_API_KEY

from .query import QUERY
