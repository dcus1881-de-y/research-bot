import requests

query = input("Ne araştırmak istiyorsun: ")

# Wikipedia arama API
search_url = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "list": "search",
    "srsearch": query,
    "format": "json"
}

response = requests.get(search_url, params=params)
data = response.json()

results = data["query"]["search"]

if not results:
    print("Sonuç bulunamadı.")
else:
    print("\nSonuçlar:\n")

    for i, result in enumerate(results[:5], start=1):
        title = result["title"]
        snippet = result["snippet"]

        print(f"{i}. {title}")
        print(snippet)
        print()
