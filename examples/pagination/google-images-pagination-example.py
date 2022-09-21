# Docs: https://serpapi.com/images-results

from serpapi import GoogleSearch
from urllib.parse import (parse_qsl, urlsplit)

params = {
    "api_key": "...",           # your serpapi api key
    "engine": "google",         # search engine
    "q": "minecraft redstone",  # search query
    "gl": "us",                 # country of the search
    "hl": "en",                 # language
    "ijn": 0,                   # page number: 0 -> first page, 1 -> second...
    "tbm": "isch"               # image results
}

search = GoogleSearch(params)   # where data extraction happens

# to show the page number
page_num = 0

image_results = []

while True:
    results = search.get_dict() # # JSON -> Python dictionary

    page_num += 1
    print(f"Current page: {page_num}")

    # checks for "Google hasn't returned any results for this query."
    if "error" not in results:
        for image in results.get("images_results", []):
            if image["original"] not in image_results:
                print(image["original"])
                image_results.append(image["original"])

        # update to the next page
        params["ijn"] += 1
    else:
        print(results["error"])
        break