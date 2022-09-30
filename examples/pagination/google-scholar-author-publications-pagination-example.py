# docs: https://serpapi.com/google-scholar-author-articles

from serpapi import GoogleScholarSearch
from urllib.parse import (parse_qsl, urlsplit)

params = {
  "api_key": "...",                     # serpapi api key
  "engine": "google_scholar_author",    # search engine
  "hl": "en",                           # language
  "author_id": "jlas1aMAAAAJ"           # search query
}

search = GoogleScholarSearch(params)    # where data extraction happens

# to show page number
page_num = 0

# iterate over all pages
results_is_present = True
while results_is_present:
    results = search.get_dict()          # JSON -> Python dict

    if "error" in results:
        print(results["error"])
        break

    page_num += 1
    print(f"Current page: {page_num}")

    # iterate over organic results and extract the data
    for result in results.get("articles", []):
        print(result.get("title"), result.get("authors"), sep="\n")

    # check if the next page key is present in the JSON
    # if present -> split URL in parts and update to the next page
    if "next" in results.get("serpapi_pagination", {}):
        search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))
    else:
        break