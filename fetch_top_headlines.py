"""
Fetches the headlines of top stories of the day
and their associated publishers/authors.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://apnews.com/"

class TopHeadlinesAPI:

    def __init__(self, num_headlines):
        self.num_headlines = num_headlines

    def fetch_headlines(self):
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")
        header_html = soup.find("div", {"class": "TopStories"}).find_all("h2", {"class": "-cardHeading"})

        headlines = []
        for header in header_html:
            text = header.contents[0]
            if (":" in text):
                text = text.split(":")[1]

            headlines.append(text.strip())

        headlines = list(set(headlines))[:self.num_headlines]

        return headlines


def main():
    th_api = TopHeadlinesAPI(3)
    print(th_api.fetch_headlines())


if __name__ == "__main__":
    main()