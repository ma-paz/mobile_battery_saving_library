import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

def scrape_multiple_pages(base_url, keyword, num_pages):
    all_results = []

    # Set up Chrome in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # This line makes Chrome run in headless mode
    driver = webdriver.Chrome(options=options)

    # Navigate to the Google Scholar page
    driver.get(base_url)
    search_box = driver.find_element("name", "q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(2)  # Adjust as needed

    # Loop through pages
    for page_number in range(1, num_pages + 1):
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract data from the current page
        results = extract_data_from_page(soup, keyword)
        all_results.extend(results)

        # Click on the next page link
        next_page_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.next-page-class'))
        )
        next_page_link.click()

        # Wait for the next page to load (you might need to adjust the wait time)
        time.sleep(2)  # Adjust as needed

    driver.quit()

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
keyword = "mobile battery"
num_pages = 3  # Set the number of pages you want to scrape
result_data = scrape_multiple_pages(base_url, keyword, num_pages)

# Save results to CSV
save_to_csv(result_data, 'output.csv')


