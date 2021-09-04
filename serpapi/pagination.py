from serpapi.serp_api_client_exception import SerpApiClientException

DEFAULT_START = 0 
DEFAULT_END = 1000000000
DEFAULT_num = 10

# Paginate response in SearpApi
class Pagination:
  
  def __init__(self, client, start = DEFAULT_START, end = DEFAULT_END, num = DEFAULT_num):
    # serp api client
    self.client = client
    # range
    self.start = start
    self.end = end
    self.num = num

    # use value from the client
    if self.start == DEFAULT_START:
      if 'start' in self.client.params_dict:
        self.start = self.client.params_dict['start']
    if self.end == DEFAULT_END:
      if 'end' in self.client.params_dict:
        self.end = self.client.params_dict['end']
    if self.num == DEFAULT_num:
      if 'num' in self.client.params_dict:
        self.num = self.client.params_dict['num']

    # basic check
    if self.start > self.end:
        raise SerpApiClientException("start: {} must be less than end: {}".format(self.start, self.end))
    if(self.start + self.num) > self.end:
        raise SerpApiClientException("start + num: {} + {} must be less than end: {}".format(self.start, self.num, self.end))

  def __iter__(self):
    self.update()
    return self

  def update(self):
    self.client.params_dict['start'] = self.start
    self.client.params_dict['num'] = self.num
    if self.start > 0:
      self.client.params_dict['start'] += 1

  def __next__(self):
    # update parameter
    self.update()

    # execute request
    result = self.client.get_dict()

    # stop if backend miss to return serpapi_pagination
    if not 'serpapi_pagination' in result:
      raise StopIteration

    # stop if no next page
    if not 'next' in result['serpapi_pagination']:
        raise StopIteration

    # ends if no next page
    if self.start + self.num > self.end:
        raise StopIteration
    
    # increment start page
    self.start += self.num

    return result
