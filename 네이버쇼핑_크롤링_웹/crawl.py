from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(
    "C:/Users/seob6/Desktop/chromedriver/chromedriver/chromedriver.exe")
driver.implicitly_wait(3)
driver.get("https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EA%B3%B5%EA%B8%B0%EC%B2%AD%EC%A0%95%EA%B8%B0&pagingIndex=1&pagingSize=10&productSet=total&query=%EA%B3%B5%EA%B8%B0%EC%B2%AD%EC%A0%95%EA%B8%B0&sort=rel&timestamp=&viewType=list")

last_height = driver.execute_script("return document.body.scrollHeight")
while 1:
    # scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # wait to load page
    driver.implicitly_wait(2)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    # driver.implicitly_wait(2)
    
    # calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        for i in soup.select("div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a"):
            print(i.text)
        break
    last_height = new_height
        
    
