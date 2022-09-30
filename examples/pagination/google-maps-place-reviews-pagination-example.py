# Docs: https://serpapi.com/maps-place-results

# For the given URL we want DATA ID parameter. Look where 👇 starts and ends. That's what we need.

# www.google.com
# maps
# place
# GameStop
# @40.70605,-74.183206,10z
# data=                          👇                                   👇 
# !4m9!1m2!2m1!1sgamestop+!3m5!1s0x89c2632baa1222a1:0xc8ccef76fb4dc917!8m2!3d40.7060247!4d-73.6558696
# 0x89c2632baa1222a1:0xc8ccef76fb4dc917
# !15sCghnYW1lc3RvcCIDiAEBWgoiCGdhbWVzdG9wkgEQdmlkZW9fZ2FtZV9zdG9yZQ

from serpapi import GoogleSearch
from urllib.parse import (parse_qsl, urlsplit)

params = {
  "api_key": "...",                                  # your serpapi api key
  "engine": "google_maps_reviews",                   # parsing engine
  "hl": "en",                                        # language of the search 
  "data_id": "0x89c251dd1776880d:0xa3ea85dca1b55baf" # place id
}

search = GoogleSearch(params)                         # where data extraction happens on the backend

# to show the page number
page_num = 0

# iterate over all pages
while True:
    results = search.get_dict()                        # JSON -> Python dict

    if "error" in results:
        print(results["error"])
        break

    page_num += 1
    print(f"Current page: {page_num}")

    # iterate over organic results and extract the data
    for result in results.get("reviews", []):
        print(result.get("user"), result.get("date"), sep="\n")

    if results.get("serpapi_pagination").get("next") and results.get("serpapi_pagination").get("next_page_token"):
        search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))
    else:
        break