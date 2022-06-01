from urllib import parse
from serpapi import constant

# Paginate response in SerpApi
class Pagination:

  def __init__(self, client, start = constant.DEFAULT_START, end = constant.DEFAULT_END, num = constant.DEFAULT_PAGE_SIZE, limit = constant.DEFAULT_LIMIT):
    # SerpApi client
    self.client = client

    self.limit = limit

    """Backwards-compatible workaround.
    `start`, `num`, and `end` parameters to `Pagination#__init__` are deprecated.

    Set `start` and `num` search parameters.
    It works for Google Search API only.
    A correct way to set an offset, limit, and page size is in search parameters directly.
    (A hash that is passed to `SerpApi#__init__`.)
    """
    if start != constant.DEFAULT_START:
      self.client.params_dict['start'] = start

    if end != constant.DEFAULT_END:
      self.client.params_dict['end'] = end

    if num != constant.DEFAULT_PAGE_SIZE:
      self.client.params_dict['num'] = num


    self.page_number = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.page_number >= self.limit:
      raise StopIteration

    # execute request
    result = self.client.get_dict()

    pagination = result.get('serpapi_pagination', result.get('pagination'))

    # stop if backend miss to return `serpapi_pagination` or `pagination`
    if not pagination:
      raise StopIteration

    # stop if no next page
    if not 'next' in pagination:
      raise StopIteration

    # Get actual parameters from next page of target website
    params_from_target_website = dict(
      parse.parse_qsl(parse.urlsplit(pagination['next']).query)
    )

    # stop if parameters from the target website were not changed
    if params_from_target_website.items() <= self.client.params_dict.items():
      raise StopIteration

    self.client.params_dict.update(params_from_target_website)

    self.page_number += 1

    return result
