import requests
import csv

def search_github_repositories(keyword, access_token=None):
    base_url = "https://api.github.com/search/repositories"
    headers = {"Authorization": f"token {access_token}"} if access_token else {}

    # Construct the API request
    params = {"q": keyword}
    response = requests.get(base_url, params=params, headers=headers)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        repositories = data.get("items", [])

        # Open a CSV file for appending
        with open('output.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')  # Use comma as the delimiter

            # Write repository data
            for repo in repositories:
                writer.writerow([repo['full_name'], repo['description']])

    else:
        print(f"Error: {response.status_code}, {response.text}")

# Example usage
token = "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"
search_github_repositories("mobile battery", token)#1
search_github_repositories("mobile energy consumption", token)#2
search_github_repositories("android battery", token)#3
search_github_repositories("ios battery saving", token)#4
search_github_repositories("movile energy saving", token)#5
search_github_repositories("bateria movil", token)#6
search_github_repositories("cuidado de bateria movil", token)#7
search_github_repositories("mantención de bateria movil", token)#8
search_github_repositories("mobile battery sustainability", token)#9
search_github_repositories("sostentabilidad dispositivo movil", token)#10
search_github_repositories("smartphone sustainability", token)#11
search_github_repositories("smartphone battery", token)#12

