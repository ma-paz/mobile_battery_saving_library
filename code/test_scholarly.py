import json
import pandas as pd
from scholarly import scholarly

# Initialize an empty list to store the data
author_data = []

# will paginate to the next page by default
authors = scholarly.search_keyword("mobile")

for author in authors:
    # Append each author's information to the list
    author_data.append(author)
    print(author)

# Create a DataFrame from the list of author data
df = pd.DataFrame(author_data)

# Save the DataFrame to an Excel file
df.to_excel("mobile battery_authors.xlsx", index=False)
