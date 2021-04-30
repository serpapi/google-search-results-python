
# Paginate response in SearpApi
class Pagination:
  def __init__(self, client, start = 0, end = 1000000000, page_size = 10):
    self.client = client
    self.start = start
    self.end = end
    self.page_size = page_size
  
  def __iter__(self):
    return self

  def __next__(self):
    # execute search
    self.client.params_dict['start'] = self.start
    result = self.client.get_dict()
    
    # quit if no next page
    if not 'next' in result['serpapi_pagination']:
        raise StopIteration

    # increment page
    self.start += self.page_size

    # ends
    if self.start > self.end:
        raise StopIteration

    return result
