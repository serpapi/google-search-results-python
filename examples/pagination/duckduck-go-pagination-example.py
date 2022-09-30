# docs: https://serpapi.com/duckduckgo-search-api

from serpapi import GoogleSearch # will be changed to DuckDuckGoSearch later

params = {
    "api_key": "...",           # your serpapi api key
    "engine": "duckduckgo",     # search engine
    "q": "minecraft redstone",  # search query
    "kl": "us-en"               # language
}

search = GoogleSearch(params)   # where data extraction happens
pages = search.pagination()     # paginating over all pages

# to show the page number
page_num = 0

for page in pages:

    # checks for "Duckduckgo hasn't retured anything for this query..."
    if "error" in page:
        print(page["error"])
        break

    page_num += 1
    print(f"Page number: {page_num}")

    for result in page["organic_results"]:
        print(result["title"])