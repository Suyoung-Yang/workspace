import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
from bs4 import BeautifulSoup

url= "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")


#
# title =cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title,"https://comic.naver.com"+ link)
#
# 만화 제목과 링크 가져오#
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title,link)


#  평점 구하기
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(cartoon.find("strong").get_text())
    total_rates += float(rate)
print("평균 점수는: ",total_rates/len(cartoons))

"""
BeautifulSoup 1:47:54 이후 강의 필요.
https://www.youtube.com/watch?v=yQ20jZwDjTE
"""
