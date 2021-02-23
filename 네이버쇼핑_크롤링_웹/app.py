from flask import Flask, render_template, request
from openpyxl.styles.differential import DifferentialStyle
import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver

wb = Workbook()
write_ws = wb.active
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/result')
def result():
    driver = webdriver.Chrome(
        "C:/Users/seob6/Desktop/chromedriver/chromedriver/chromedriver.exe")
    driver.implicitly_wait(3)
    driver.get("https://search.shopping.naver.com/search/all?query=%EA%B3%B5%EA%B8%B0%EC%B2%AD%EC%A0%95%EA%B8%B0&cat_id=&frm=NVSHATC")
    html = driver.page_source()
    soup = BeautifulSoup(html, 'lxml')

    titles = []
    # imgs =
    for title in soup.select("div.basicList_info_area__17Xyo"):
        print(title[0])

        # return render_template("result.html")


if __name__ == '__main__':
    app.run()
