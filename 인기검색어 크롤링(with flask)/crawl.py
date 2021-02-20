import re
import requests
from bs4 import BeautifulSoup
import feedparser  # rss 피드 파싱 위해 feedparser import.

url = 'https://trends.google.co.kr/trends/trendingsearches/daily/rss?geo=KR'
feed = feedparser.parse(url)


def today_date():
    for i, j in enumerate(feed['entries']):
        if i == 0:
            today_date = j['published']
            today_date = today_date.split(' ')[3] + ' ' + today_date.split(' ')[2] + ' ' + \
                today_date.split(' ')[1] + ' ' + today_date.split(' ')[0]
            today_date = today_date[:-1]
            return today_date
        else:
            break


def today_title():
    today_title = []
    for content in feed['entries']:
        if today_date().split()[0] and today_date().split()[1] and today_date().split()[2] in content['published']:
            today_title.append(content['title'])
        else:
            break
    return today_title

def url():
    url = []
    for content in feed['entries']:
        if today_date().split()[0] and today_date().split()[1] and today_date().split()[2] in content['published']:
            url.append(content['ht_news_item_url'])
        else:
            break
    return url

def link_content():
    link_content = []
    for content in feed['entries']:
        if today_date().split()[0] and today_date().split()[1] and today_date().split()[2] in content['published']:
            link = content['ht_news_item_url']
            if '&#39;' or '&nbsp;' or '&quot;' in content['ht_news_item_title']:
                title = content['ht_news_item_title'].replace(
                    '&#39;', '').replace('&nbsp;', '').replace('&quot;', '')
            else:
                title = content['ht_news_item_title']
            if '&#39;' or '&nbsp;' or '&quot;' in content['ht_news_item_snippet']:
                snippet = content['ht_news_item_snippet'].replace(
                    '&#39;', '').replace('&nbsp;', '').replace('&quot;', '')
            else:
                snippet = content['ht_news_item_snippet']
            link_content.append([title, link, snippet])
        else:
            break
    return link_content
