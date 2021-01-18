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

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a.get_text()) #soup 객체에서 처음 발견되는 a
# print(soup.a.attrs) # a element의 속성 정보
# print(soup.a["href"]) # a element의 href 속성 정보


# print(soup.find("a", attrs = {"class":"Nbtn_upload"}))
print(soup.find(attrs = {"class":"Nbtn_upload"})) # 원하는 태그를 명시하지 않아도 된다.

print(soup.find("li",attrs={"class":"rank01"}))
# rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a)
# print(rank1.a.get_text())
# print(rank1.next_sibling.next_sibling) # 태그사이 개행이 있더라 (해당 사이트에)
# # rank2 = rank1.next_sibling.next_sibling
# rank3 = rank1.next_sibling.next_sibling.next_sibling.next_sibling
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank3.get_text)
# print(rank2.get_text)
# print(rank1.parent.get_text)
#
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())


# rank1.find_next_siblings("li") # 형제 들 가져오기
# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a",text = "재혼 황후-64화")
print(webtoon)
