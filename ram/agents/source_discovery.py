import requests
from bs4 import BeautifulSoup


def search_web(query):
    url = "https://www.google.com/search"

    params = {
        "q": query
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for result in soup.select("div.tF2Cxc")[:5]:
        title = result.select_one("h3")
        link = result.select_one("a")

        if title and link:
            results.append({
                "title": title.get_text(),
                "url": link.get("href")
            })

    return results
