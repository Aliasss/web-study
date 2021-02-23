import requests
from bs4 import BeautifulSoup

keyword = input()
page = int(input())

for i in range(1, page+1):
    req = requests.get(
        f"https://search.daum.net/search?nil_suggest=sugsch&w=news&DA=PGD&cluster=y&q={keyword}&p={i}")
    soup = BeautifulSoup(req.text, 'lxml')
    titles = soup.select("a.f_link_b")
    links = soup.select(".wrap_tit > a")

    for title, link in zip(titles, links):
        print(title.text)
        print(link['href'])
        print('-----------')
