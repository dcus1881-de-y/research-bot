import requests
from bs4 import BeautifulSoup

query = input("Ne araştırmak istiyorsun: ")

url = f"https://duckduckgo.com/html/?q={query}"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("a", class_="result__a", limit=5)

print("\nSonuçlar:\n")

for r in results:
    print("-", r.text)
