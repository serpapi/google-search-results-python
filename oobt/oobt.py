import sys
import os
from serpapi import GoogleSearchResults

# Run Out Of Box testing
#  Load package
#  Run simple query
#
import pprint
print("initialize serpapi search")
search = GoogleSearchResults({
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
        print("OK: Out out box testing is passing")
        sys.exit(0)

print("FAIL: Out box testing is failing: no result")
sys.exit(1)
