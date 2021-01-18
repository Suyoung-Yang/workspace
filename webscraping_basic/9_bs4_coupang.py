import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=5&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

res = requests.get(url,headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
#
#
items = soup.find_all("li",attrs= {"class":re.compile("^search-product")})
print(items[0].find("div",attrs = {"class":"name"}).get_text())

for item in items:
    name = item.find("div",attrs = {"class":"name"}).get_text()
    price = item.find("strong",attrs={"class":"price-value"}).get_text()

    rate= item.find("em",attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"

    rate_count= item.find("em",attrs={"class":"rating-total-count"})
    if rate_count:
        rate_count = rate_count.get_text()
    else:
        rate_count = "평점 없음"

    print(name, price, rate, rate_count)
