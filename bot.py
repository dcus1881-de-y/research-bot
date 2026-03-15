import requests

def search_wikipedia(query):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query

    response = requests.get(url)

    if response.status_code != 200:
        print("Sonuç bulunamadı.")
        return

    data = response.json()

    title = data.get("title", "Başlık yok")
    summary = data.get("extract", "Açıklama yok")

    print("\n📚 Başlık:", title)
    print("\n🧠 Özet:\n")
    print(summary)


query = input("Ne araştırmak istiyorsun: ")

query = query.replace(" ", "_")

search_wikipedia(query)
