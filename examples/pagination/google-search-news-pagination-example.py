# docs: https://serpapi.com/news-results

from serpapi import GoogleSearch
from urllib.parse import (parse_qsl, urlsplit)

params = {
    "api_key": "...",           # serpapi api key
    "engine": "google",         # search engine
    "q": "minecraft",           # search query
    "gl": "us",                 # country of the search
    "hl": "en",                 # language
    "num": "100",               # number of news per page
    "tbm": "nws"                # news results
}

search = GoogleSearch(params)   # where data extraction happens

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
    for result in results.get("news_results", []):
        print(result.get("position"), result.get("title"), sep="\n")

    if "next" in results.get("serpapi_pagination", {}):
        search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))
    else:
        break