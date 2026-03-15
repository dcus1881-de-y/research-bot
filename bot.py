import requests

query = input("Ne araştırmak istiyorsun: ")

url = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "list": "search",
    "srsearch": query,
    "format": "json"
}

response = requests.get(url, params=params)

try:
    data = response.json()
except:
    print("Veri okunamadı. İnternet veya API hatası olabilir.")
    exit()

results = data.get("query", {}).get("search", [])

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
