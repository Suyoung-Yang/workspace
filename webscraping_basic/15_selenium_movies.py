import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


import requests
from bs4 import BeautifulSoup

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
"Accept-Language":"ko-KR,ko" # 한국어가 있는 경우, 한국어로 출력해달라.
}
url = "https://play.google.com/store/movies/top"

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

movies = soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
# print(len(movies))

"""
# header없이 정보를 가져오게 되는 경우, 구글은 미국 기준으로 기본값 정보들을 출력해줌
# header를 넣어야 현재 해당 사용자가 웹에서 보고 있는 화면을 볼 수 있음.
with open("movie.html","w",encoding="utf8") as f:
    # f.write(res.text)
    f.write(soup.prettify()) # html문서를 예쁘게 출력
"""
# WsMG1c nnK0zc
for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)
