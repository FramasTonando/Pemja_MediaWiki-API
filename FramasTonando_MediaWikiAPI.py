import requests

def search_wikipedia(query):
    endpoint = "https://en.wikipedia.org/w/api.php"

    # pencarian artikel
    search_params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query
    }

    try:
        # mengirim metode get melalui api
        response = requests.get(endpoint, params=search_params)
        response.raise_for_status()  # pesan http error jika tidak mendapat respon

        # hasil pencarian
        search_results = response.json()["query"]["search"]

        if not search_results:
            print("Tidak ada hasil dari query yang diberikan")
            returnn            

        # menampilkan hasil pencarian
        for result in search_results:
            title = result["title"]
            page_id = result["pageid"]
            page_link = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
            
            print(f"Title: {title}")
            print(f"Link: {page_link}")
            print()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # contoh pencarian
    search_wikipedia("One Piece")
