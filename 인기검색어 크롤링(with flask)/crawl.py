import requests
from bs4 import BeautifulSoup
import feedparser  # rss 피드 파싱 위해 feedparser import.

# req = requests.get('https://trends.google.co.kr/trends/trendingsearches/daily/rss?geo=KR')
# soup = BeautifulSoup(req.text, 'lxml')

# def date_func():
#     date = soup.select_one('item > pubDate').text
#     return date

# date_func()

url = 'https://trends.google.co.kr/trends/trendingsearches/daily/rss?geo=KR'
feed = feedparser.parse(url)
print(feed['entries'])

