# Docs: https://serpapi.com/ebay-search-api

from serpapi import EbaySearch
from urllib.parse import (parse_qsl, urlsplit)

params = {
    "api_key": "...",              # serpapi api key    
    "engine": "ebay",              # search engine
    "ebay_domain": "ebay.com",     # ebay domain
    "_nkw": "minecraft redstone",  # search query
    # other params
}

search = EbaySearch(params)        # where data extraction happens

page_num = 0

while True:
    results = search.get_dict()     # JSON -> Python dict

    if "error" in results:
        print(results["error"])
        break
    
    for organic_result in results.get("organic_results", []):
        title = organic_result.get("title")
        print(title)
        
    page_num += 1
    print(page_num)
    
    # {'_nkw': 'minecraft redstone', '_pgn': '19', 'engine': 'ebay'}
    next_page_query_dict = dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)) 
    current_page = results["serpapi_pagination"]["current"] # 1,2,3...

    # looks for the next page data (_pgn):
    # {'_nkw': 'minecraft redstone', '_pgn': '19', 'engine': 'ebay'}
    if "next" in results.get("pagination", {}):
        
        # if current_page = 20 and next_page_query_dict["_pgn"] = 20: break
        if int(current_page) == int(next_page_query_dict["_pgn"]):
            break
        
        # update next page data
        search.params_dict.update(next_page_query_dict)
    else:
        break
    