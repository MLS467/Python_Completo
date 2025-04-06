import requests
import bs4  # type:ignore

url = "https://g1.globo.com/"

content_news = requests.get(url)
raw_content = content_news.text
parserd_content_news = bs4.BeautifulSoup(raw_content, "html.parser")

selector = (
    "div> "
    "div.feed-post-body-title.gui-color-primary.gui-color-hover "
    "> div > h2 > a > p"
)

result = parserd_content_news.select(selector)

for index, new in enumerate(result):
    link = new.parent["href"]
    if link is not None:
        print(f"{index}. {new.text.strip()}")
        print(f"🔗 Link: {link}\n")
