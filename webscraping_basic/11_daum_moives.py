"""

다음 영화 페이지에서 최근 n년간 인기있었던 영화들 이미지를 가져오기.
이미지를 가져오려 직접 페이지에 들어가보니, 여러번 클릭해야 이미지를 가지고 올 수 있음


"""

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}



for year in range(2015,2020):
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")

    images = soup.find_all("img",attrs={"class":"thumb_img"})
    # image 불러오기. https 가 없을 경우에는 추가해서 프린트하기.
    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:"+image["src"]

        print(image_url)
        image_res = requests.get(image_url)# 페이지에 접속해서 파일로 저장하기 위해
        image_res.raise_for_status()

        # 이미지 가져오기, 대신 모두 가지고 오게 됨.
        with open("movie_{}_{}.jpg".format(year,idx+1), "wb") as f:
            f.write(image_res.content)
        if idx>=4: break # 상위 5개만 가지고 오기 위해
