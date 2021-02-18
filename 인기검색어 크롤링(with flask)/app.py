from flask import Flask, render_template
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

@app.route('/')
def hello():

    req = requests.get('https://trends.google.co.kr/trends/trendingsearches/daily?geo=KR')
    soup = BeautifulSoup(req.text, 'lxml')
    print(soup)

    return render_template('index.html')

@app.route('/about')
def about():
    return "여기는 about"

if __name__ == '__main__':
    app.run()