import requests
import csv
from datetime import datetime
from dotenv import gitAPI

def search_github_and_save(query, access_token, filename='github_repositories.csv', append=False):
    url = "https://api.github.com/search/repositories"
    headers = {"Authorization": f"Bearer {access_token}"}

    params = {"q": query, "sort": "stars", "order": "desc"}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        repositories = data.get("items", [])

        if repositories:
            # Prepare data for CSV
            rows = []
            for repo in repositories:
                row = [repo['name'], repo['description'], repo['updated_at'],
                       repo['size'], repo['language']]
                rows.append(row)

            # Determine whether to append or create a new file
            mode = 'a' if append else 'w'

            # Save data to CSV
            with open(filename, mode, newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                if not append:
                    # Write header row for a new file
                    header = ['Name', 'Description', 'Last Update', 'Size (KB)', 'Language']
                    writer.writerow(header)

                # Write data rows
                writer.writerows(rows)

            print(f"Data for '{query}' saved successfully.")
        else:
            print(f"No repositories found for '{query}'.")
    else:
        print(f"Error: {response.status_code}")


# Example usage

token = gitAPI

search_github_and_save("mobile battery", token, append=True)#1
search_github_and_save("mobile energy consumption", token, append=True)#2
search_github_and_save("android battery", token, append=True)#3
search_github_and_save("ios battery saving", token, append=True)#4
search_github_and_save("movile energy saving", token, append=True)#5
search_github_and_save("bateria movil", token, append=True)#6
search_github_and_save("cuidado de bateria movil", token, append=True)#7
search_github_and_save("mantención de bateria movil", token, append=True)#8
search_github_and_save("mobile battery sustainability", token, append=True)#9
search_github_and_save("sostentabilidad dispositivo movil", token, append=True)#10
search_github_and_save("smartphone sustainability", token, append=True)#11
search_github_and_save("smartphone battery", token, append=True)#12

