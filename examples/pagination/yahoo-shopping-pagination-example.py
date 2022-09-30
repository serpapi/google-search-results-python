# docs: https://serpapi.com/yahoo-shopping-search-api

from serpapi import YahooSearch

params = {
    "api_key": "...",           # serpapi api key
    "engine": "yahoo_shopping", # search engine
    "p": "redstone"             # search query
}

search = YahooSearch(params)    # where data extraction happens
pages = search.pagination()     # paginates over all pages

page_num = 0

for page in pages:

    if "error" in page:
        print(page["error"])
        break

    page_num += 1
    print(f"Current page: {page_num}")

    for result in page.get("shopping_results", []):
        print(result["title"])