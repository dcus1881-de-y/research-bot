import requests
from bs4 import BeautifulSoup

query = input("Ne araştırmak istiyorsun: ")

url = f"https://duckduckgo.com/html/?q={query}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

results = soup.select("a.result__a")

print("\nSonuçlar:\n")

for r in results[:5]:
    print("-", r.get_text())
