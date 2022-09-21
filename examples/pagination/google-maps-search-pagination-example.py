# docs: https://serpapi.com/maps-local-results

from serpapi import GoogleSearch
from urllib.parse import (parse_qsl, urlsplit)

params = {
  "api_key": "...",                    # serpapi api key
  "engine": "google_maps",             # search engine
  "type": "search",                    # type is set to search. there's also place search type.
  "q": "gamestop",                     # search query
  "hl": "en",                          # language
  "ll": "@40.7107323,-74.1542422,10z"  # GPS coordinates of location where you want your q (query) to be applied.
}

search = GoogleSearch(params)          # where data extraction happens

# to show the page number
page_num = 0

# iterate over all pages
results_is_present = True
while results_is_present:
    results = search.get_dict()       # JSON -> Python dict      

    if "error" in results:
        print(results["error"])
        break

    page_num += 1
    print(f"Current page: {page_num}")

    # iterate over organic results and extract the data
    for result in results.get("local_results", []):
        print(result.get("position"), result.get("title"), result.get("gps_coordinates"), result.get("address"), sep="\n")

    # check if the next page key is present in the JSON
    # if present -> split URL in parts and update to the next page
    if "next" in results.get("serpapi_pagination", {}):
        search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))
    else:
        break