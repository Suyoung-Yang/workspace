
# 한글 출력 위한 처리
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# import
import requests
from bs4 import BeautifulSoup


# url에서 정보가져오기
finding = "%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={}".format(finding)
res = requests.get(url) # requests.(url, headers = headers) / headers는 user-agent 정보 넣기
res.raise_for_status() # 문제가 되는지 확인, 200이 아닐경우 headers를 넣어서 문제 없애기

soup = BeautifulSoup(res.text,"lxml") # 가져온 res의 text정보를 lxml형태로 BeautifulSoup에 넣기

# print(soup.title) # title정보 가져오기
# print(soup.title.get_text()) # title에서 text만 가져오기.

# 테이블에서 각 행 가져오기
data_rows = soup.find("table",attrs={"class":"tbl"}).find("tbody").find_all("tr")
for idx,row in enumerate(data_rows):
    columns = row.find_all("td")
    print("="*10,"매물{}".format(idx+1),"="*10)
    print("거래 : ",columns[0].get_text().strip())
    print("면적 : ",columns[1].get_text().strip(), "(공급/면적)")
    print("가격 : ",columns[2].get_text().strip(), "(만원)")
    print("동 : ",columns[3].get_text().strip())
    print("층 : ",columns[4].get_text().strip())




"""
with open("quiz.htlm","w",encoding="utf8") as f:
    f.write(soup.prettify())
"""



# data = [column.get_text().strip() for column in columns]
# print(data)
# col1 = soup.find("td", attrs={"class":"col1"})
# cols = [[0]*6]
# for i in range(1,6):
#     col = soup.find("td",attrs={"class":"col{}".format(i)})
#     print(col.get_text(),end=' ')
# # col1s = soup.find_all("td",attrs={"class":"col1"})
#
# for col1 in col1s:
#     print(col1.get_text())
