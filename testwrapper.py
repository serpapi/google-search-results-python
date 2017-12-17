from serpwrapper import QUERY
import sys

class NotEnoughArgsError(Exception):
    pass
def test_query():
    """Tests an API call to get a HTML content"""
    params = {}
    if len(sys.argv) < 3 :
        raise NotEnoughArgsError(
            "SERP API requires user to put in Query and Location as command-line arguments"
        )
    params['query'] = sys.argv[1]
    params['location'] = sys.argv[2]
    if len(sys.argv) == 4:
        params['ui_lang'] = sys.argv[3]
    if len(sys.argv) == 5:
        params['country'] = sys.argv[4]
    if len(sys.argv) == 6:
        params['num_results'] = sys.argv[5] if sys.argv[5] else None
    # print query, location
    query_instance = QUERY(None)
    return query_instance.retrieve_html(params)

    # assert isinstance(response, dict)
    # assert response['id'] == 1396, "The ID should be in the response"

test_query()
