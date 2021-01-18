import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
from bs4 import BeautifulSoup


url= "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a",attrs={"class":"title"})
for cartoon in cartoons:
    print(cartoon.get_text())


# 가우스 전자 내용 가져오기
