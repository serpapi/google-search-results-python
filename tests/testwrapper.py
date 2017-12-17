from ..serpwrapper import QUERY

def test_query():
    """Tests an API call to get a HTML content"""

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should be in the response"
