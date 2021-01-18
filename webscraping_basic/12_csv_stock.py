"""
네이버에서 금융정보 가져오기
"""
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import csv # csv 파일로 저장용
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# 파일 정하기
filename = "시가총액1-200.csv"

f = open(filename,"w",encoding="utf-8-sig",newline="") # 엑셀파일에서 한글 깨질 때, utf-8-sig,newline은 csv파일에서 row 안 떨어지게 하기 위해
writer = csv.writer(f)
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t") # 단순히 복붙 + tab으로 구분

writer.writerow(title)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: continue # 의미 없는 데이터 스킵
        data = [column.get_text().strip() for column in columns]
        # print(data)/
        writer.writerow(data)
