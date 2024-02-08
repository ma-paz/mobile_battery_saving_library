from serpapi import GoogleSearch
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

key = os.getenv("SERPAPI_KEY")
params = {
    "api_key": key,
    "engine": "google_scholar",
    "q": "mobile energy saving patterns",
    "hl": "en",
    "start":370,
    "num": "20",
    "as_ylo": "2015"
}

search = GoogleSearch(params)
results = search.get_dict()

# Extract relevant information from the search results
search_results = results.get("organic_results", [])

# Initialize lists to store data
titles = []
links = []
descriptions = []

# Extract data from search results
for result in search_results:
    title = result.get("title", "")
    link = result.get("link", "")
    description = result.get("snippet", "")

    titles.append(title)
    links.append(link)
    descriptions.append(description)

# Create a DataFrame from the lists
df = pd.DataFrame({"Title": titles, "Link": links, "Description": descriptions})

# Save the DataFrame to an Excel file
df.to_excel("serpapi_37.xlsx", index=False)