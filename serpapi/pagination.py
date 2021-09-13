from serpapi.serp_api_client_exception import SerpApiClientException
from urllib.parse import urlsplit, parse_qsl
from serpapi.constant import *

class PaginationKeys:
  def set_keys(self, engine):
    # set default
    self.start_key = "start"
    self.num_key = "num"
    self.end_key = "end"

    # override per search engine
    if engine == BAIDU_ENGINE:
      self.start_key = "pn"
      self.num_key = "rn"
    elif engine == BING_ENGINE:
      self.start_key = "pn"
      self.num_key = "rn"
    elif engine == YAHOO_ENGINE:
      self.start_key = "b"
      self.num_key = "pz"
    elif engine == YANDEX_ENGINE:
      self.start_key = "p"
    elif engine == EBAY_ENGINE:
      self.start_key = "_pgn"
      self.num_key = "_ipg"
    elif engine == WALMART_ENGINE:
      self.start_key = "page"
      self.num_key = "ps"
    elif engine == HOME_DEPOT_ENGINE:
      self.start_key = "nao"
    # TODO youtube ?

# Paginate response in SearpApi
class Pagination(PaginationKeys):
  
  def __init__(self, client, start = DEFAULT_START, end = DEFAULT_END, num = DEFAULT_PAGE_SIZE, engine = "google"):
    # register parent client
    self.client = client

    # set pagination variables
    self.start = start
    self.end = end
    self.num = num

    # set search key based on seach engien
    self.set_keys(engine)

    # use value from the client if available
    if self.start == DEFAULT_START:
      if 'start' in self.client.params_dict:
        self.start = self.client.params_dict[self.start_key]
    if self.end == DEFAULT_END:
      if self.end_key in self.client.params_dict:
        self.end = self.client.params_dict[self.end_key]
    if self.num == DEFAULT_PAGE_SIZE:
      if self.num_key in self.client.params_dict:
        self.num = self.client.params_dict[self.num_key]

    # basic check
    if self.start > self.end:
        raise SerpApiClientException("start: {} must be less than end: {}".format(self.start, self.end))
    if(self.start + self.num) > self.end:
        raise SerpApiClientException("start + num: {} + {} must be less than end: {}".format(self.start, self.num, self.end))

  def __iter__(self):
    return self
  
  def __next__(self):
    # execute request
    result = self.client.get_dict()

    # stop if backend miss to return serpapi_pagination
    if not 'serpapi_pagination' in result:
      raise StopIteration

    # stop if no next page
    serpapi_pagination = result['serpapi_pagination']
    if not 'next' in serpapi_pagination:
        raise StopIteration
    
    # increment start page
    try:
      split = urlsplit(serpapi_pagination['next'])
      parameter = dict(parse_qsl(split.query))
      print(split.query)
      self.client.params_dict.update(parameter)
    except:
      raise SerpApiClientException("pagination fail to decode: response.serpapi_pagination.next = " + serpapi_pagination['next'])

    # stop iterative
    if self.stop():
        # TODO remove debug statement
        print("DEBUG: stop: start:" + self.client.params_dict[self.start_key] + " < end : " + str(self.end) )
        raise StopIteration
    else:
        # TODO remove debug statement
        print("DEBUG: continue: start:" + self.client.params_dict[self.start_key] + " < end : " + str(self.end) )

    return result

  def stop(self):
    start = int(self.client.params_dict[self.start_key])
    return start > self.end