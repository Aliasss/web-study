from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/seob6/Desktop/chromedriver/chromedriver/chromedriver.exe")
driver.implicitly_wait(3)
driver.get("https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=공기청정기&pagingIndex=2&pagingSize=10&productSet=total&query=공기청정기&sort=rel&timestamp=&viewType=list")
html = driver.page_source()
soup = BeautifulSoup(html, 'lxml')

for title in soup.select("a.basicList_link__1MaTN"):
    print(title.text)