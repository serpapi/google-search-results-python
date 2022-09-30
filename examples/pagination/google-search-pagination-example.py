# docs: https://serpapi.com/organic-results

from serpapi import GoogleSearch

params = {
    "api_key": "...",           # serpapi api key
    "engine": "google",         # search engine
    "q": "minecraft redstone",  # search query
    "gl": "us",                 # country of the search
    "hl": "en"                  # language
}

search = GoogleSearch(params)   # where data extraction happens
pages = search.pagination()     # paginates over all pages

# to show page number
page_num = 0

# iterate over all pages
for page in pages:

    if "error" in page:
        print(page["error"])
        break

    page_num += 1
    print(f"Current page: {page_num}")

    # iterate over organic results and extract the data
    for result in page["organic_results"]:
        print(result["position"], result["title"], sep="\n")