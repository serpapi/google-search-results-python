# docs: https://serpapi.com/google-jobs-api

from serpapi import GoogleSearch
import json

params = {
    "api_key": "...",                   # serpapi api key
    "engine": "google_jobs",            # parsing engine
    "google_domain": "google.com",      # google domain for the search
    "q": "Barista",                     # search query
    "start": 0                          # page number
}

search = GoogleSearch(params)           # where data extraction happens on the backend

jobs_data = []

# to show page number
page_num = 0

while True:
    results = search.get_dict()         # JSON -> Python dict
    
    # checks for "Google hasn't returned any results for this query."
    if "error" in results:
        print(results["error"])
        break

    page_num += 1
    print(f"Current page: {page_num}")

    # iterate over organic results and extract the data
    for result in results["jobs_results"]:
        jobs_data.append({
            "title": result["title"],
            "company_name": result["company_name"],
            "location": result["location"]
        })

    params["start"] += 10

print(json.dumps(jobs, indent=2))