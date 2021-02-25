from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(
    "C:/Users/seob6/Desktop/chromedriver/chromedriver/chromedriver.exe")
driver.implicitly_wait(3)
driver.get("https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=공기청정기&pagingIndex=1&pagingSize=20&productSet=total&query=공기청정기&sort=rel&timestamp=&viewType=list")

last_height = driver.execute_script("return document.body.scrollHeight")
while 1:
    # scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(2)
    
    # calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select("div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a")
        links = soup.select("div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a")
        for title, link in zip(titles, links):
            print(link['href'])
        break
    last_height = new_height
            
    
