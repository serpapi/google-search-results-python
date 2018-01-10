# Google Search Results in Python

This Python package is meant to scrape and parse Google results using [SERP API](https://serpapi.com). Feel free to fork this repository to add more backends.

## Simple Example

    query = GoogleSearchResults.new q: "coffee"
    hash_results = query.get_hash

## Set SERP API key

    GoogleSearchResults.serp_api_key = "Your Private Key"
Or

    query = GoogleSearchResults.new q: "coffee", serp_api_key: "Your Private Key"

## Example with all params and all outputs

    query_params = {
      q: "query",
      google_domain: "Google Domain",
      location: "Location Requested",
      device: device,
      hl: "Google UI Language",
      gl: "Google Country",
      safe: "Safe Search Flag",
      num: "Number of Results",
      start: "Pagination Offset",
      serp_api_key: "Your SERP API Key"
    }

    query = GoogleSearchResults.new query_params
    query.params[:location] = "Portland"

    html_results = query.get_html
    hash_results = query.get_hash
    hash_results_with_images = query.get_hash_with_images
    json_results = query.get_json
    json_results_with_images = query.get_json_with_images

## Example of Python Dictionary Output (GoogleSearchResults#get_hash)
