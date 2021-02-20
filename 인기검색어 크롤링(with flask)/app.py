import enum
import requests
from bs4 import BeautifulSoup
import feedparser  # rss 피드 파싱 위해 feedparser import.
from flask import Flask, render_template
import crawl

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/detail')
def detail():
    today_date = crawl.today_date()
    today_title = crawl.today_title()
    link_content = crawl.link_content()
    url = crawl.url()

    return render_template('detail.html',
                           date=today_date, 
                           title=today_title, 
                           content=link_content,
                           url = url,
                           length = len(link_content),
                           enumerate = enumerate)


if __name__ == '__main__':
    app.run()
