# docs: https://serpapi.com/shopping-results

from serpapi import GoogleSearch
from urllib.parse import (parse_qsl, urlsplit)

params = {
    "api_key": "...",           # serpapi api key
    "engine": "google",         # search engine
    "q": "minecraft",           # search query
    "gl": "us",                 # country of the search
    "hl": "en",                 # language
    "num": "100",               # number of results per page
    "tbm": "shop"               # shopping results
}

search = GoogleSearch(params)   # where data extraction 

# to show page number
page_num = 0

# iterate over all pages
while True:
    results = search.get_dict()  # JSON -> Python dict

    if "error" in results:
        print(results["error"])
        break

    page_num += 1
    print(f"Current page: {page_num}")

    # iterate over organic results and extract the data
    for result in results.get("shopping_results", []):
        print(result.get("position"), result.get("title"), result.get("price"), sep="\n")

    if "next" in results.get("serpapi_pagination", {}):
        search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))
    else:
        break