from serpapi import GoogleSearch

params = {
  "api_key": "3dfc42cfc42e2f182d041fe334210a81a507338d4fceecea53a064266f461d51",
  "engine": "google_scholar",
  "q": "Coffee",
  "hl": "en"
}

search = GoogleSearch(params)
results = search.get_dict()
print(results)