from serpapi import GoogleSearch
from dotenv import serpapiAPI

params = {
  "api_key": serpapiAPI,
  "engine": "google_scholar",
  "q": "Coffee",
  "hl": "en"
}

search = GoogleSearch(params)
results = search.get_dict()
print(results)