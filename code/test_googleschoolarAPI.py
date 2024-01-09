import requests
from bs4 import BeautifulSoup
import csv

def scrape_multiple_pages(base_url, params, keyword):
    all_results = []

    # Loop through pages
    page_number = 1
    while True:
        # Create a new dictionary for each page to avoid modifying the original params
        page_params = params.copy()
        page_params['page'] = page_number

        response = requests.get(base_url, params=page_params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract data from the current page
            results = extract_data_from_page(soup, keyword)
            all_results.extend(results)

            # Check if there's a next page
            next_page_link = soup.find('a', {'class': 'next-page-class'})
            if not next_page_link:
                break  # Break the loop if no next page link is found

            page_number += 1
        else:
            print(f"Error: {response.status_code}")
            break  # Break the loop on error

    return all_results

def extract_data_from_page(soup, keyword):
    # Extract information based on the HTML structure of the Google Scholar page
    titles = [title.text for title in soup.find_all('h3', class_='gs_rt')]
    authors = [author.text for author in soup.find_all('div', class_='gs_a')]
    abstracts = [abstract.text for abstract in soup.find_all('div', class_='gs_rs')]

    # Return the extracted results
    return list(zip(titles, authors, abstracts))

def save_to_csv(results, filename='output.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header row
        writer.writerow(['Title', 'Authors', 'Abstract'])

        # Write data rows
        for result in results:
            writer.writerow(result)

# Example usage
base_url = "https://scholar.google.com/scholar"
params = {'q': 'mobile'}
keyword = "mobile battery"
result_data = scrape_multiple_pages(base_url, params, keyword)

# Save results to CSV
save_to_csv(result_data, 'output.csv')


