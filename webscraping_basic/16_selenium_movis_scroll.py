import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


"""

"""

from selenium import webdriver
browser = webdriver.Chrome()
# browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,1080)") # 윈도우에서 세로 방향으로 1080(본인 컴퓨터 해상도)위치로 내려라..
# browser.execute_script("window.scrollTo(0,2080)")

# 화면 가장 아래로 스크롤 내리기

# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time
interval = 5

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤을 가장 먼저 아래로
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(interval)
    current_height = browser.execute_script("return document.body.scrollHeight")
    if current_height == prev_height:
        break

    prev_height = current_height
print("scroll 완료")


# 스크래핑 작업 실시
# 원래는 import 구문은 위에 있는 것이 문법에 맞다.

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source,"lxml")

# movies = soup.find_all("div",attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]}) # 클래스 2개로 찾기
movies = soup.find_all("div",attrs={"class":"Vpfmgd"})

# print(len(movies))

# WsMG1c nnK0zc 영화들의 class
# SUZt4c djCuy 할인가격이 있는 영화는 해당 class를 갖는다.
# VfPpfd ZdBevf i5DZme 할인가격 클래스
# JC71ub는 영화 link
for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)
    original_price = movie.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title,"할인되지 않은 영화 제외")
        continue

    # 할인된 가격
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a",attrs={"class":"JC71ub"})["href"]
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com"+link)
    print("-"*120)

browser.quit()
