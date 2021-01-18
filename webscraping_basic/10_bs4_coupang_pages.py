"""

여러 페이지를 돌면서 정보 스크래핑

"""

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

for i in range(1,6): # 1부터 5페이지까지
    # print("페이지",i)


    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)


    res = requests.get(url,headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    items = soup.find_all("li",attrs= {"class":re.compile("^search-product")})

    for item in items:

        #광고 제품은 제외
        ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("광고 상품은 제외합니다.")
            continue

        name = item.find("div",attrs = {"class":"name"}).get_text()

        # 애플 제품은 제외
        if "Apple" in name:
            # print("<apple 상품 제외합니다.>")
            continue

        price = item.find("strong",attrs={"class":"price-value"}).get_text()

        # 리뷰 100개 이상, 평점 4.5 이상 되는것만 조회

        rate= item.find("em",attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()

        else:
            rate = "평점 없음"
            # print("평점 없는 상품은 제외합니다")
            continue

        rate_count= item.find("span",attrs={"class":"rating-total-count"})
        if rate_count:
            rate_count = rate_count.get_text()[1:-1]
            # print("리뷰수",rate_count)
        else:
            rate_count = "평점 수 없음"
            # print("평점 없는 상품은 제외합니다.")
            continue

        link = item.find("a",attrs = {"class":"search-product-link"})["href"]

        if float(rate)>=4.5 and int(rate_count)>=100:
            print(name, price, rate, rate_count)
            print(f"제품명: {name}")
            print(f"가격: {price}")
            print(f"평점: {rate}점 ({rate_count})")
            print("바로가기: {}".format("https://www.coupang.com" + link))
            print("-"*100) # 줄긋기




# 광고 붙은 내용은 없애보자..
