import requests
from bs4 import BeautifulSoup  # type: ignore


url = "http://localhost:8000/html/#home"

response_ = requests.get(url)

raw_html = response_.text
parsed_html = BeautifulSoup(raw_html, "html.parser")

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

# all_tags_p = parsed_html.select("img")
all_tags_p = parsed_html.select_one("#intro > div > div > article > h2")

if all_tags_p is not None:
    print(all_tags_p.parent)

# for i in all_tags_p:
#     print(i)
