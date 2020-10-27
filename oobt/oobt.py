import sys
import os
from serpapi import GoogleSearch

# Run Out Of Box testing
#  Load package
#  Run simple query
#
import pprint
print("initialize serpapi search")
search = GoogleSearch({
        "q": "coffee",
        "location": "Austin,Texas", 
        "api_key": os.getenv("API_KEY","demo")
})
print("execute search")
result = search.get_dict()
print("display result")
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(result)
print("------")
if len(result) > 0:
        print("OK: Out of box tests passed")
        sys.exit(0)

print("FAIL: Out of box tests failed: no result")
sys.exit(1)
