from . import session

class QUERY(object):
    def __init__(self, params_dict):
        self.params_dict = params_dict
    def retrieve_html(self, params_dict):
        path = 'https://serpapi.com/search?q=' + params_dict['query'] + '&location=' + params_dict['location']
        print "the full request path is\n\t\t\t\t", path
        response = session.get(path)
        return response.text
