# docs: https://serpapi.com/bing-search-api

from serpapi import BingSearch
from urllib.parse import (parse_qsl, urlsplit)

params = {
    "api_key": "...",        # your serpapi api key
    "engine": "bing",        # parsing engine
    "q": "brabus",           # search query         
    "device": "desktop",     # device used for search
    "mkt": "en-us",          # language of the search
    "count": "50"            # number of results per page. 50 is the maximum
}

search = BingSearch(params)   # where data extraction happens 

while True:
    results = search.get_dict() # JSON -> Python dict

    if "error" in results:
        print(results["error"])
        break

    # iterate over organic results and extract the data
    for result in results["organic_results"]:
        print(result["position"], result["title"], sep="\n")

    # check if the next page key is present in the JSON
    # if present -> split URL in parts and update to the next page
    if "next" in results.get("serpapi_pagination", {}):
        search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination", {}).get("next")).query)))
    else:
        break