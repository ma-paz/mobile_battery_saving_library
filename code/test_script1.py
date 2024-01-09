import requests

def search_github_code(keyword, repository, access_token=None):
    base_url = "https://api.github.com/search/code"
    headers = {"Authorization": f"token {access_token}"} if access_token else {}

    # Construct the API request
    params = {"q": f"{keyword} repo:{repository}"}
    response = requests.get(base_url, params=params, headers=headers)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])

        # Display code snippets
        for item in items:
            print(f"File: {item['name']}")
            print(f"Path: {item['path']}")
            print(f"Snippet:\n{item['text']}")
            print("-" * 30)
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Example usage
search_github_code("battery", "tobykurien/BatteryFu", "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")
