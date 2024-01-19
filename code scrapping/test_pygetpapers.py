import os
import json
import pandas as pd
from pygetpapers import getpapers, download

# Set your query
query = "mobile battery"

# Create a directory for storing the papers
outdir = "papers_output"

# Fetch papers based on the query
getpapers(query, outdir)

# Download the full text PDFs
download(outdir)

# Initialize lists to store paper titles and abstracts
paper_titles = []
paper_abstracts = []

# Now, you can read the downloaded papers and extract titles and abstracts
# Extracting titles and abstracts depends on the format of the downloaded papers and may require additional parsing.

# Example: Extract titles and abstracts
for paper_id in os.listdir(outdir):
    with open(os.path.join(outdir, paper_id, paper_id + ".json"), "r") as f:
        paper_data = json.load(f)
        title = paper_data.get("title", "No title available")
        abstract = paper_data.get("abstract", "No abstract available")
        
        # Append titles and abstracts to the lists
        paper_titles.append(title)
        paper_abstracts.append(abstract)

# Create a DataFrame from the lists
df = pd.DataFrame({"Paper Title": paper_titles, "Abstract": paper_abstracts})

# Save the DataFrame to an Excel file
df.to_excel("papers_info.xlsx", index=False)
